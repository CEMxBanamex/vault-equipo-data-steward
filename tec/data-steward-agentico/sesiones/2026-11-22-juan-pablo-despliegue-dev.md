---
tipo: sesion
fecha: 2026-11-22
autor: juan-pablo
resumen: Infraestructura de dev aplicada en el Learner Lab y primer despliegue automático completo (backend en EC2 con migraciones, frontend en Vercel), con los arreglos que pidió el lab; S1-05, S1-07 y S1-10 listas.
---
# Sesión 2026-11-20 al 22: infraestructura de dev y primer despliegue

Trabajo con Claude Code en el repo de código y en el vault, del 20 al 22 de noviembre. La nota se escribió el 23. Sigue a [[tec/data-steward-agentico/sesiones/2026-11-17-juan-pablo-fases-0-a-3-infra-ci-cd|fases 0 a 3]].

## Qué se hizo
| Paso | Resultado |
|---|---|
| Entorno local en una Mac (Apple Silicon) con Docker Desktop | `make up`, `make migrate` y `make datos` funcionan; pasan las 245 pruebas de datos y las del backend, el grafo y el MCP |
| S1-07 sin el socio formador | [[tec/data-steward-agentico/plan-de-trabajo/decision-supuestos-sin-socio-formador\|Decisión: supuestos sin el socio formador]], con las políticas de facturas basadas en el SAT |
| Terraform `bootstrap` | Bucket del estado con versionado, cifrado y sin acceso público |
| Terraform `shared` | 31 recursos: VPC, security groups, RDS PostgreSQL 16, presupuesto de 20 USD y el parámetro de la llave de Tailscale |
| `scripts/db/crear-bases.sh` | 5 roles de servicio, 7 usuarios personales y las bases `dsa_dev` y `dsa_prod`; contraseñas en SSM, sin imprimirse |
| Llave de Tailscale para AWS | Reutilizable, no efímera, `tag:aws`, guardada en SSM |
| Terraform `dev` | 21 recursos: EC2 `t3.small` con IP elástica, bucket de archivos y 13 parámetros de SSM |
| Arranque de la EC2 | user-data sin errores; `dsa-arranque` la unió a la tailnet como `dsa-dev` y generó el `.env` desde SSM |
| DNS en Hostinger | Registro A de `api-dev` hacia la IP elástica y CNAME de `dev` hacia Vercel |
| Fase 5 (PR 16 del repo de código) | Fusionado; variable `DOMINIO`, secretos de Vercel, runner `dsa-dev` registrado por Session Manager y `RUNNER_DEV_ACTIVO=true` |
| Primer despliegue completo | Imágenes en GHCR, migraciones en `dsa_dev` (versión 0003, 36 tablas), contenedores `backend`, `mcp` y `caddy` sanos, frontend en Vercel con el alias de dev |

**URLs de dev** (se actualizan solas en cada merge a `dev`):
- Frontend: `https://dev.cem-steward.online`
- API: `https://api-dev.cem-steward.online` (salud en `/api/health`)

**PR del repo de código:** 23 (Terraform y script aplicables en el lab), 25 (`--debug` temporal), 26 y 27 (alias de Vercel).

## Problemas y cómo se resolvieron
| Problema | Causa | Solución |
|---|---|---|
| `bootstrap` creó el bucket pero fallaron sus otros recursos con `AccessDenied` | Una SCP del lab niega `s3:GetBucketObjectLockConfiguration` y el recurso `aws_s3_bucket` la lee siempre al crear o refrescar | Los buckets (`bootstrap` y `modules/s3`) se crean y se borran con la CLI de AWS desde un `terraform_data`; Terraform los lee con el data source, que no consulta Object Lock, y sigue administrando su configuración |
| El `plan` de `dev` fallaba con *Unsupported attribute* | Con Cognito apagado, los outputs `cognito_*` de `shared` son `null` y no existen en el estado remoto | `dev` y `prod` los leen con `try(..., null)` |
| `crear-bases.sh` no corría en macOS | Usaba `mapfile` y arreglos asociativos, que no existen en el bash 3.2 de macOS | Reescrito sin esas funciones; mismo comportamiento |
| Las llamadas a Secrets Manager tardaban 7 minutos o fallaban con *Signature expired* | La red anunciaba IPv6 pero no lo enrutaba; la CLI de AWS prueba primero las direcciones IPv6 del endpoint (SSM no tiene, por eso era rápido) | `--cli-connect-timeout 3`, o desactivar IPv6 en esa red. Quedó en el README de Terraform |
| EC2 Instance Connect no conectaba | Las EC2 no tienen SSH abierto, a propósito | Se entra por **Session Manager** (consola de EC2 → Conectar → Administrador de sesiones) |
| La EC2 no podía bajar las imágenes (`unauthorized`) | GHCR crea los paquetes privados y la organización no permitía paquetes públicos | Se permitieron en la configuración de la organización y los dos paquetes quedaron públicos (no llevan secretos ni datos) |
| `vercel deploy` fallaba con *Project not found* | `VERCEL_ORG_ID` tenía el ID de usuario; Vercel pasó las cuentas personales a un "equipo personal" con ID `team_…` | Se tomó el `orgId` de `vercel link` (archivo `.vercel/repo.json` o `project.json`) |
| El paso de Vercel fallaba con un `Error:` vacío | Con `--debug` se vio que el despliegue sí se creaba; fallaba `vercel alias` con *User not found*: ese comando siempre carga el usuario y el token está limitado a la cuenta (aun con `--scope`) | El alias se asigna con la API REST de Vercel (PR 27) |
| `dev.cem-steward.online` pedía iniciar sesión en Vercel | *Deployment Protection* activado en los despliegues de preview | Se desactivó en el proyecto de Vercel |

## Decisiones
Las de infraestructura y CI/CD quedaron como actualización del 2026-11-22 en [[tec/data-steward-agentico/arquitectura/decision-infraestructura-en-learner-lab|infraestructura en Learner Lab]] y [[tec/data-steward-agentico/arquitectura/decision-ramas-y-ci-cd|ramas y CI/CD]]. En resumen:
- Buckets creados con la CLI por la SCP del lab.
- Paquetes de GHCR públicos.
- Alias de dev con la API de Vercel.
- Sin acceso por SSH: todo por Session Manager y SSM Run Command.

## Aprendizajes
- **Lo que el lab sí permite:** contraseña maestra de RDS en Secrets Manager, AWS Budgets y SSM Run Command (del que depende el despliegue a prod).
- **`set_config` en RDS:** se confirmó el aviso de `crear-bases.sh`: `steward_consultas` todavía puede ejecutar `set_config` en `dsa_dev` y `dsa_prod`. La defensa queda en la validación del SQL de `ejecutar_consulta` (S1-08).
- **El lab se apaga y todo vuelve solo:** al encender, `dsa-arranque` reconecta Tailscale, regenera el `.env` y levanta la versión de `/dsa/dev/image_tag`; el runner vuelve como servicio.
- **Vercel asigna solo el dominio de la rama:** como `dev.cem-steward.online` está ligado a la rama `dev` en el proyecto, Vercel ya lo apuntaba a cada despliegue; el workflow lo asigna de forma explícita para no depender de eso.
- **Logs de Actions desde una red con IPv6 roto:** `ghcr.io` y el servidor de logs de GitHub no respondían desde la Mac; los logs se leen en la web.

## Pendientes
- **Ollama en dev:** `/dsa/dev/ollama_base_url` sigue en `CAMBIAR`. Falta la IP de Tailscale de la laptop que sirve los modelos (Carlos Ramos tiene Ollama expuesto, S1-29).
- **Una sola URL de Ollama:** el código y Terraform aceptan una sola (`OLLAMA_BASE_URL`), pero el [[tec/data-steward-agentico/modelos/inventario-gpus-y-reparto-modelos|reparto de modelos]] reparte visión, chat y embeddings en tres laptops. O una laptop sirve todo, o el frente de agentes agrega una URL por rol.
- **Tailnet:** según las llaves, solo los dos Carlos entraron. Mario, Yael, Iris, Mauricio y Juan Pablo tienen su llave sin usar.
- **Prod:** aplicar `envs/prod` y fusionar `dev` → `main` (PR 12 del repo de código) para probar `deploy-prod.yml`.
- **Cierre del 24 de noviembre:** base privada y Cognito (S1-09).
- **Lucid:** actualizar el diagrama (sin ALB, Caddy e IP elástica, frontend en Vercel).
- **Datos en dev:** `deploy.sh` solo corre migraciones, así que `dsa_dev` tiene las 36 tablas pero no los datos sintéticos. Falta un script que cargue los datos sintéticos en RDS con el usuario `steward_carga` (en local es `make datos`, que no se puede repetir; para recargar, `make reset-db`).
- **Avisos del CI:** las acciones `checkout` y `setup-node` en Node 20 están obsoletas.

## Siguiente paso
Conectar Ollama en dev con la IP de Tailscale de Carlos Ramos, cargar los datos sintéticos en `dsa_dev` y preparar la sesión de contratos (S1-06), que ya solo espera la S1-39 de Mauricio.
