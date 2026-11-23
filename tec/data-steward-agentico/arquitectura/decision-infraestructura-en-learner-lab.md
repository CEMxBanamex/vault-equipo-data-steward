---
tipo: decision
fecha: 2026-11-10
autor: juan-pablo
resumen: Infraestructura del MVP ajustada a AWS Learner Lab y al cierre de noviembre - EC2 de dev y prod detrás de un ALB compartido, RDS con pgvector, S3, SSM, imágenes en GHCR, frontend en Vercel y dominio propio fuera de AWS.
---
# Decisión: infraestructura del MVP en AWS Learner Lab

- **Contexto:**
  - La cuenta de AWS es de **Learner Lab**: la sesión dura 4 horas y al expirar se detienen las EC2; no se pueden crear roles de IAM ni proveedores OIDC (solo existen `LabRole` y `LabInstanceProfile`); las credenciales cambian en cada sesión, y el presupuesto son los créditos del lab (si se acaban, se pierde todo).
  - El proyecto debe quedar terminado antes de que acabe noviembre de 2026.
  - El frontend va en Vercel, que sirve por HTTPS, así que la API también necesita HTTPS (si no, el navegador bloquea las llamadas por *mixed content*).
- **Decisión:** ver las secciones de abajo.
- **Por qué:** es lo más simple que funciona dentro de las restricciones del lab, cuida los créditos y deja todo reproducible por si la cuenta se reinicia.
- **Enlaces:** [[tec/data-steward-agentico/arquitectura/_index|arquitectura]], [[tec/data-steward-agentico/arquitectura/decision-ramas-y-ci-cd|Decisión: ramas y CI/CD]], [[tec/data-steward-agentico/arquitectura/guia-claude-code-ci-cd|Guía para Claude Code]], [[tec/data-steward-agentico/arquitectura/decision-jwt-al-final|Decisión: JWT al final]]

## Componentes
| Tema | Decisión |
|---|---|
| Frontend | Vercel, desplegado desde GitHub Actions con la CLI (sin despliegue automático por Git) |
| Backend | Docker Compose con dos contenedores, `backend` y `mcp`, en EC2 |
| Registro de imágenes | GitHub Container Registry (GHCR), paquetes públicos |
| Base de datos | Una instancia RDS PostgreSQL 16 con pgvector y dos bases: `dsa_dev` y `dsa_prod` |
| Archivos | Un bucket S3 privado por ambiente, con URLs prefirmadas |
| Balanceador | Un solo ALB para dev y prod, con reglas por subdominio |
| Dominio | Comprado fuera de AWS; el DNS vive en el registrador |
| Secretos | SSM Parameter Store (SecureString); la contraseña maestra de RDS la administra RDS en Secrets Manager |
| Permisos | Las EC2 usan `LabInstanceProfile`; no se crean roles |
| Infraestructura como código | Terraform, aplicado por Juan Pablo desde su computadora con las credenciales del lab |
| GPUs | Ollama en las laptops del equipo vía Tailscale |
| Auth | `AUTH_MODE=dev` hasta la última semana; después Cognito |

## Ambientes
| Ambiente | Frontend | Backend | Base | Se actualiza |
|---|---|---|---|---|
| local | Vite en la laptop | `docker-compose.dev.yml` | Postgres + pgvector en Docker, MinIO como S3 | Siempre |
| dev | `dev.<dominio>` | `api-dev.<dominio>` → EC2 dev | `dsa_dev` | Automático en cada push a la rama `dev` |
| prod | `app.<dominio>` | `api.<dominio>` → EC2 prod | `dsa_prod` | Al fusionar `dev` → `main` |

**El trabajo diario es local.** El lab solo lo enciende Juan Pablo y se apaga cada 4 horas: si el equipo dependiera de la base en AWS, se bloquearía. AWS dev sirve para integrar y probar juntos.

## Red
```
Internet
 ├── app / dev.<dominio> ──► Vercel
 └── api / api-dev.<dominio> (CNAME en el registrador)
          ▼
 VPC (una región del lab, 2 zonas)
  Subredes públicas
   ALB: HTTPS con certificado de ACM, reglas por subdominio,
        idle timeout 300 s, SG solo IPs del equipo hasta activar Cognito
     ├── target group dev  ──► EC2 dev  (backend + mcp + runner de GitHub)
     └── target group prod ──► EC2 prod (backend + mcp)
   SG de las EC2: entrada solo desde el ALB, sin SSH (acceso por SSM Session Manager)
  Subredes privadas
   RDS PostgreSQL + pgvector, SG: entrada solo desde las EC2
 S3 por ambiente · SSM Parameter Store · Cognito (fase 4) · AWS Budgets
 EC2 ──Tailscale──► laptops con Ollama (solo puerto 11434)
```

## Detalle por recurso
- **EC2:** Amazon Linux 2023, x86_64 (`t3.small` o `t3.medium`, para no construir imágenes multiarquitectura). En subred pública con IP pública, para salir a internet sin NAT; el security group solo acepta tráfico del ALB. IMDSv2 obligatorio. `user-data.sh` instala Docker, Compose, Tailscale y deja servicios que arrancan solos después de cada reinicio del lab.
- **Se empieza con EC2 sueltas, una por ambiente.** El ASG se agrega solo si la prueba de cómo se comporta con el lab apagado sale bien; la arquitectura sigue permitiéndolo porque las réplicas son idénticas.
- **ALB:** puerto 443 con certificado de ACM para `api` y `api-dev`; el 80 redirige a 443. Health check en `/api/health`. Idle timeout de 300 s por el SSE del chat.
- **RDS:** `db.t4g.micro`, cifrada, en subredes privadas. Por ambiente, un usuario para el backend y otro con permisos mínimos para el MCP.
- **S3:** bloqueo de acceso público, cifrado, CORS para los dominios del frontend y `localhost`. VPC Gateway Endpoint de S3 (no tiene costo).
- **Tailscale:** la key de las instancias es reutilizable, **no efímera**, con `tag:aws`, para que sobreviva los reinicios. ACL: solo `tag:aws → tag:gpu:11434`.
- **Terraform:** estado en un bucket S3 del lab con `use_lockfile` y respaldo local. Prohibido crear recursos de IAM.
- **Presupuesto:** alertas de AWS Budgets al 50, 80 y 100 %.

## Qué cambia respecto a lo propuesto (2026-10-21 y 2026-10-28)
- Sin contenedor `frontend` ni Nginx: el frontend va en Vercel y el ALB apunta directo al `backend`.
- EC2 en subred pública (cerrada por security group) en vez de privada, para no pagar NAT. RDS sigue privada.
- Ya no hay roles de IAM por definir: se usa `LabInstanceProfile`.
- Secretos en SSM Parameter Store en vez de Secrets Manager, salvo la contraseña maestra de RDS.
- Imágenes en GHCR en vez de ECR, y despliegue con un runner self-hosted en vez de *instance refresh*. Ver [[tec/data-steward-agentico/arquitectura/decision-ramas-y-ci-cd|ramas y CI/CD]].
- Un solo ALB y una sola RDS para dev y prod.

## Alternativas descartadas
- **NAT Gateway:** costo fijo alto para los créditos del lab. Si se quiere volver a EC2 privadas, la opción barata es fck-nat.
- **ngrok:** sirve para exponer servicios hacia afuera (entrada), no le da salida a internet al EC2. Para Ollama lo dejaría en una URL pública; Tailscale se queda.
- **CloudFront sin dominio:** da HTTPS gratis, pero obliga a desactivar el caché de la API con cuidado, mover la restricción por IP y vigilar los timeouts del SSE.
- **Rewrites de Vercel como proxy:** el tramo hacia AWS iría sin cifrar con los JWT y la restricción por IP dejaría de servir.
- **Route 53 para el dominio:** la cuenta del lab es temporal; el dominio y su DNS deben quedar fuera de ella.
- **ECR con OIDC:** el lab no permite OIDC ni roles, y sus credenciales caducan.

## Riesgos
| Riesgo | Mitigación |
|---|---|
| El lab se apaga a media demo o prueba | Encenderlo con anticipación; todo arranca solo |
| Se acaban los créditos | Budgets, sin NAT, una RDS y un ALB, apagar lo que no se use |
| Se reinicia o borra la cuenta del lab | Todo en Terraform, migraciones y scripts del piloto; dominio fuera de AWS |
| El equipo depende del lab de Juan Pablo | Trabajo diario en local |
| Cognito se integra tarde | Activarlo con días de margen |

## Pendiente verificar en el lab
- Que ACM y Cognito estén permitidos.
- Qué servicios siguen cobrando con el lab apagado (probablemente ALB y RDS).
- Que `LabRole` permita SSM Run Command y escribir en Parameter Store.
- Cómo se comporta un ASG cuando el lab detiene las instancias.


## Actualización 2026-11-10 (acceso a la base, usuarios y datos)
- **RDS pública temporal**, para que el equipo se conecte con DBeaver o pgAdmin sin Tailscale:
  - `publicly_accessible = true`, en las subredes públicas.
  - Security group con el 5432 abierto desde una variable (`db_allowed_cidrs`, por defecto `0.0.0.0/0`).
  - Conexión cifrada obligatoria (`rds.force_ssl = 1`; en el cliente, `sslmode=require`).
  - **Se cierra el 24 de noviembre**, junto con Cognito: `publicly_accessible = false`, 5432 solo desde las EC2 y sin escritura personal en prod. Queda documentado en el README como decisión temporal.
- **RDS solo está disponible con el lab encendido.** El trabajo diario es con la base local; para probar en dev, Juan Pablo enciende el lab en **ventanas de integración** acordadas (dos o tres por semana) o cuando alguien lo pide.
- **Usuarios de la base.** Los roles de Postgres son de toda la instancia, así que existen con el mismo nombre en `dsa_dev` y `dsa_prod`; los permisos se dan por base. Se acepta para el proyecto.

| Usuario o grupo | `dsa_dev` | `dsa_prod` |
|---|---|---|
| `steward_migraciones` (dueño del esquema, solo para migraciones) | Estructura | Estructura |
| `steward_backend`, `steward_mcp` | Los de la aplicación | Los de la aplicación |
| `steward_consultas` (consulta libre, solo vistas, 5 s) | Solo `SELECT` en vistas | Solo `SELECT` en vistas |
| `steward_carga` (script de datos) | Cargar datos | Cargar datos |
| Grupo `equipo_lectura`: un usuario por integrante | Leer | Leer |
| Grupo `equipo_datos`: Iris y Mario | Leer y escribir datos | Leer |
| Usuario maestro | Solo Juan Pablo | Solo Juan Pablo |

- Los nombres `steward_backend`, `steward_mcp` y `steward_consultas` son los que ya usan las migraciones del frente de datos. Infraestructura los crea **antes** de correr las migraciones, como pide [[tec/data-steward-agentico/tools/propuesta-vistas-para-consulta-libre-mario|la propuesta de Mario]]; las migraciones solo otorgan permisos.
- Los usuarios personales leen las tablas directamente, sin la seguridad por fila de las vistas. Está bien porque los datos son sintéticos.
- **En RDS el usuario maestro no es superusuario.** El `REVOKE` de `set_config` de la migración `0003` puede no tener efecto (la migración avisa con un `WARNING`). Revisarlo en la primera migración contra dev; si no aplica, la lista blanca de funciones en la validación del SQL es la defensa principal.
- **Datos:**
  - La estructura solo cambia con migraciones, en todos los ambientes. Nadie la cambia desde una interfaz.
  - Los datos sintéticos viven en el repo y se cargan con las semillas del frente de datos (`make datos`), igual en cada laptop.
  - A prod se cargan con el mismo script y la misma versión, primero en dev. En prod nadie inserta ni edita a mano.
- **Descartado:** pgAdmin web con login de Cognito en el ALB y DBeaver por Tailscale (demasiado para un proyecto escolar), y versionar los datos en S3 para el entorno local (el equipo no tiene acceso al lab).


## Actualización 2026-11-17 (Terraform escrito y cambios por créditos)
Sesión: [[tec/data-steward-agentico/sesiones/2026-11-17-juan-pablo-fases-0-a-3-infra-ci-cd|fases 0 a 3]]. Reemplaza lo que choque de arriba.

- **Sin ALB ni certificado de ACM.** Al 11 de noviembre quedaban 26 USD de créditos, y el ALB cobra aunque el lab esté apagado.
  - El HTTPS lo da **Caddy** en cada EC2, con un certificado de Let's Encrypt.
  - Cada EC2 tiene una **IP elástica**, así el registro A del dominio no cambia cuando el lab se apaga.
  - En el registrador: registros **A** de `api-dev` y `api` hacia las IP elásticas, en vez de CNAME al ALB y validación de ACM.
  - Security group de cada EC2: el 80 abierto (validación del certificado y redirección) y el 443 desde `allowed_cidrs_<env>`.
  - Costo estimado del 17 al 30 de noviembre: de 11 a 13 USD. Alertas de gasto en 8, 14 y 20 USD.
- **API abierta a internet** (`0.0.0.0/0`) mientras `AUTH_MODE=dev`, porque el equipo cambia de red e IP. Se acepta porque los datos son sintéticos y no hay tool para liberar pagos. Se cierra con Cognito.
- **RDS siempre en las subredes públicas.** El cierre es solo `db_publica = false` y `db_allowed_cidrs = []`. Cambiar su subnet group recrearía la instancia.
- **Cognito:** solo un administrador crea las cuentas (nadie se registra solo).
- **Disco de las EC2:** 20 GB en vez de 30.
- **Estado:** el Terraform está en `infra/terraform/` del repo de código, con el `plan` verificado contra la cuenta. Todavía no se aplica nada.
- **Pendiente verificar en el lab** (actualiza la lista de arriba):
  - ACM ya no se usa.
  - Falta confirmar que RDS pueda guardar la contraseña maestra en Secrets Manager y que AWS Budgets esté permitido.


## Actualización 2026-11-22 (aplicado en el lab)
Sesión: [[tec/data-steward-agentico/sesiones/2026-11-22-juan-pablo-despliegue-dev|infraestructura de dev y primer despliegue]]. Reemplaza lo que choque de arriba.

- **Aplicado:** `bootstrap`, `shared` y `dev`. `prod` sigue sin aplicar hasta la primera promoción.
- **Verificado en el lab** (cierra la lista de pendientes de arriba):
  - RDS guarda la contraseña maestra en Secrets Manager.
  - AWS Budgets está permitido: el presupuesto se creó con sus alertas (8, 14 y 20 USD) al correo configurado.
  - SSM Run Command funciona con `LabInstanceProfile`, así que el despliegue a prod por SSM es viable.
- **Buckets de S3 con la CLI.** Una SCP del lab niega `s3:GetBucketObjectLockConfiguration`, y el recurso `aws_s3_bucket` de Terraform la lee siempre. Los buckets se crean y se borran con la CLI de AWS desde un `terraform_data`; Terraform los lee con el data source y administra su configuración. Quien aplica necesita la CLI de AWS.
- **Sin SSH.** Se entra a las EC2 por Session Manager; EC2 Instance Connect no funciona porque el puerto 22 está cerrado a propósito.
- **`set_config` en RDS:** confirmado que `steward_consultas` puede ejecutarlo en `dsa_dev` y `dsa_prod`. La defensa principal es la validación del SQL de `ejecutar_consulta` (S1-08).
- **DNS en Hostinger:** registro A de `api-dev` hacia la IP elástica de dev y CNAME de `dev` hacia Vercel. Faltan `api` (al aplicar prod) y `app`.


## Actualización 2026-11-23 (Ollama en dev y parámetros manuales)
Sesión: [[tec/data-steward-agentico/sesiones/2026-11-23-juan-pablo-semana-3-y-subida-s3|semana 3 y subida a S3]]. Reemplaza lo que choque de arriba.
- **Ollama en dev:** `/dsa/dev/ollama_base_url` apunta a la laptop de Carlos Ramos por Tailscale y responde desde `dsa-dev`. La ACL de la tailnet deja pasar `dsa-dev` a esa laptop.
- **Parámetro manual nuevo:** `/dsa/dev/mcp_dev_usuario = dev-ana`, creado con la CLI y fuera de Terraform. Si se recrea `envs/dev`, hay que volver a crearlo. El contenedor `mcp` lo recibe por `env_file: .env`, sin cambiar `deploy/docker-compose.yml`.
- **Pruebas desde la EC2:** SSM Run Command sirve también para probar dev sin abrir el sitio desde otra red (se usó para S3-04).
- **Red del trabajo de Juan Pablo:** bloquea el dominio del proyecto ("Connection reset by peer"). El ensayo y la demo van desde una red personal. No se instala Tailscale en equipos ni redes de trabajo.
