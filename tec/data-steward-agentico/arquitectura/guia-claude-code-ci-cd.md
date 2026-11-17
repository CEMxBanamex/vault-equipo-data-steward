---
tipo: guia
fecha: 2026-11-10
autor: juan-pablo
resumen: Instrucciones por fases para que Claude Code implemente en el repo de código la infraestructura con Terraform y el CI/CD (ramas, GitHub Actions, despliegue a EC2 y Vercel), con reglas, criterios de terminado y pasos manuales.
---
# Guía para Claude Code: infraestructura y CI/CD en el repo

Copia este archivo al repo de código (sugerido: `docs/ci-cd/guia-claude-code.md`) y pídele a Claude Code que lo siga **una fase a la vez**. Las decisiones de fondo están en [[tec/data-steward-agentico/arquitectura/decision-infraestructura-en-learner-lab|infraestructura en Learner Lab]] y [[tec/data-steward-agentico/arquitectura/decision-ramas-y-ci-cd|ramas y CI/CD]].

## Contexto
- **Monorepo:** `frontend/` (Vite + React), `backend/` (FastAPI + LangGraph, cliente MCP), `mcp/` (servidor MCP con las tools), `contracts/` (OpenAPI, eventos SSE, firmas de tools), `db/migrations/` (Alembic).
- **Repo público** en una organización de GitHub. Usa siempre los marcadores `<ORG>`, `<REPO>`, `<DOMINIO>` y `<REGION>`; nunca escribas el nombre del socio formador.
- **Ramas:** `<nombre>/<tarea>` → `dev` (despliega a dev) → `main` (promueve a prod).
- **AWS es Learner Lab:**
  - Prohibido crear `aws_iam_role`, `aws_iam_policy`, `aws_iam_instance_profile`, `aws_iam_openid_connect_provider` o usuarios de IAM. Usa `data "aws_iam_instance_profile" "lab" { name = "LabInstanceProfile" }`.
  - Las credenciales son temporales: nunca van en GitHub ni en archivos.
  - Las EC2 se detienen cuando termina la sesión (4 h): todo debe arrancar solo al encender.
  - Instancias hasta tamaño `large` y una sola región.
- **Fecha límite:** todo terminado antes de que acabe noviembre de 2026. Prefiere lo simple que funciona.

## Reglas de trabajo
1. Trabaja en ramas `jp/<tarea>`. El primer PR (Fases 1 y 2) va a `main` porque `dev` todavía no existe; después, todo va a `dev`.
2. Nunca escribas secretos, tokens, contraseñas, IDs de cuenta ni cadenas de conexión reales. Usa SSM Parameter Store, secretos de GitHub o marcadores. `.env` siempre en `.gitignore`; solo se versiona `.env.example`.
3. **Pide confirmación antes de ejecutar** `terraform apply` o `destroy`, comandos `gh api` que cambien la configuración del repo y comandos `aws` que creen o modifiquen recursos. Muéstrame primero el plan o el comando.
4. Antes de cerrar cada fase, valida: `actionlint`, `terraform fmt -check` y `terraform validate`, `shellcheck`, `hadolint` y `docker compose config`.
5. No escribas lógica de la aplicación (agentes, tools, endpoints de negocio): es de otros integrantes. Si el pipeline necesita algo que no existe (por ejemplo `/api/health`), crea lo mínimo y avísame.
6. Al terminar cada fase, dime qué archivos creaste, cómo lo probaste y qué pasos manuales me tocan.

## Fase 1: base del repo y entorno local
- `.gitignore`, `.gitattributes` (LF), `.env.example` con todas las variables documentadas y sin valores reales, y `Makefile` con `up`, `down`, `logs`, `lint`, `test`, `fmt` y `migrate`.
- **Variables:** `DATABASE_URL`, `MCP_DATABASE_URL`, `AUTH_MODE`, `OLLAMA_BASE_URL`, `MCP_URL`, `S3_BUCKET`, `S3_ENDPOINT_URL` (solo local), `AWS_REGION`, `CORS_ORIGINS`, `COGNITO_USER_POOL_ID`, `COGNITO_CLIENT_ID`.
- `docker-compose.dev.yml`:
  - `postgres` con `pgvector/pgvector:pg16`, volumen, healthcheck y script de inicio que crea la extensión `vector`.
  - `minio` como S3 local, con un servicio que crea el bucket.
  - `backend` y `mcp` con build local, recarga en caliente y `depends_on` con condición de salud.
  - El frontend corre con `npm run dev` fuera de Docker.
- `backend/Dockerfile` y `mcp/Dockerfile`: multi-stage, Python slim, usuario no root, `HEALTHCHECK`.
- Sección "Levantar en local" en el `README.md`.
- **Listo cuando:** `make up` levanta todo en una laptop limpia, `/api/health` responde 200 y la extensión `vector` existe.

## Fase 2: CI y reglas del repo
- `.github/workflows/ci.yml`, en `pull_request` hacia `dev` y `main` y en `push` a `dev`:
  - `changes`: `dorny/paths-filter` para saber qué carpetas cambiaron.
  - `backend` y `mcp`: ruff, mypy y pytest con un service container `pgvector/pgvector:pg16`.
  - `frontend`: `npm ci`, eslint, `tsc --noEmit`, vitest y `vite build`.
  - `contracts`: regenera los tipos de TypeScript desde el OpenAPI (`openapi-typescript`) y falla con `git diff --exit-code`.
  - `docker-build`: buildx sin push, con caché de GitHub Actions.
  - `secrets`: gitleaks.
  - `origen-main`: solo en PR a `main`; falla si `github.head_ref` no es `dev`.
  - `ci-ok`: job final con `if: always()` que falla si algún job necesario falló. Es el único check obligatorio.
- `.github/dependabot.yml`: pip, npm, github-actions y docker, semanal, con `target-branch: dev`.
- `.github/CODEOWNERS` por carpeta (con marcadores de usuario) y `.github/pull_request_template.md`.
- `scripts/github/configurar-repo.sh` con `gh api`, **para que yo lo ejecute** después de revisarlo:
  - Crear la rama `dev` desde `main`.
  - Ruleset de `dev`: PR obligatorio sin aprobaciones, check `ci-ok`, rama al día, solo squash, sin force push ni borrado.
  - Ruleset de `main`: PR obligatorio con 1 aprobación, revisión de code owners, descartar aprobaciones viejas, check `ci-ok`, solo merge commit, sin force push ni borrado.
  - Environments `dev` y `prod` (sin aprobación).
- **Listo cuando:** un PR de prueba a `dev` corre el CI y un PR de una rama distinta de `dev` hacia `main` queda bloqueado.

## Fase 3: infraestructura con Terraform
Estructura: `infra/terraform/bootstrap` (bucket del estado, estado local), `modules/` y tres raíces:
- `envs/shared`: VPC, security groups, ALB, certificado de ACM, RDS y Budgets.
- `envs/dev` y `envs/prod`: EC2, target group y regla del ALB, bucket S3 y parámetros de SSM de cada ambiente. Leen `shared` con `terraform_remote_state`.

Módulos:
- **network:** VPC /16, 2 zonas, 2 subredes públicas y 2 privadas, Internet Gateway, **sin NAT**, VPC Gateway Endpoint de S3.
- **security:** SG del ALB (443 y 80 desde `var.allowed_cidrs`), SG de las EC2 (8000 solo desde el SG del ALB; salida libre) y SG de RDS (5432 solo desde el SG de las EC2).
- **alb:** listener 80 que redirige a 443; listener 443 con el certificado y respuesta 404 por defecto; idle timeout de 300 s. Reglas por `host_header` hacia el target group de cada ambiente, con health check en `/api/health`.
- **acm:** certificado para `api.<DOMINIO>` y `api-dev.<DOMINIO>` con validación por DNS. Saca como output los registros de validación para que yo los copie en el registrador del dominio. **Sin Route 53.**
- **rds:** PostgreSQL 16, `db.t4g.micro`, subredes privadas, cifrado, `manage_master_user_password = true`, respaldo de 1 día.
- **s3:** un bucket por ambiente, bloqueo de acceso público, cifrado SSE-S3 y CORS (`PUT` y `GET` desde el dominio del frontend del ambiente y `http://localhost:5173`).
- **ec2:** Amazon Linux 2023 x86_64, `t3.small` por defecto, subred pública con IP pública, IMDSv2 obligatorio, `LabInstanceProfile`, disco gp3 de 30 GB, etiquetas `Env` y `Runner=true` solo en dev, y `user_data` desde una plantilla. Sin ASG por ahora.
- **ssm:** parámetros `/dsa/<env>/...` creados con el valor `CAMBIAR` y `lifecycle { ignore_changes = [value] }`; los valores reales los pongo yo con la CLI.
- **budget:** límite mensual con alertas por correo al 50, 80 y 100 %.
- **cognito** (detrás de `var.enable_cognito`, para la última semana): user pool con login por correo, grupos según los roles del producto y cliente sin secreto con las URLs de callback del frontend.
- **Backend del estado:** S3 con `use_lockfile = true`.
- **Listo cuando:** `terraform plan` sale limpio en las tres raíces, no hay recursos de IAM y los outputs incluyen el DNS del ALB y los registros de validación.

## Fase 4: despliegue en las instancias
- `deploy/docker-compose.yml`:
  - Servicios `backend` (publica el 8000) y `mcp` (solo red interna).
  - Imágenes `ghcr.io/<org>/<repo>/backend:${IMAGE_TAG}` y `.../mcp:${IMAGE_TAG}` (en minúsculas).
  - `restart: unless-stopped`, `env_file: /opt/dsa/.env`, healthchecks y rotación de logs.
- `deploy/user-data.sh`:
  - Instala Docker y el plugin de Compose.
  - Instala Tailscale y se une con la key de `/dsa/shared/tailscale_authkey`, hostname `dsa-<env>` y `tag:aws`, solo si no está unido.
  - Crea el servicio de systemd `dsa-arranque`: en cada arranque regenera `/opt/dsa/.env` desde SSM y levanta Compose con el `image_tag` vigente.
- `deploy/deploy.sh <tag> <env> [--sin-migraciones]`:
  1. Regenera `.env` desde SSM y guarda el tag anterior.
  2. Ejecuta `docker compose pull`.
  3. Corre las migraciones con `docker compose run --rm backend alembic upgrade head`.
  4. Ejecuta `up -d` y revisa la salud en `localhost:8000/api/health` con reintentos.
  5. Si funciona, escribe el tag en `/dsa/<env>/image_tag`. Si falla, regresa al tag anterior y termina con error.
- `scripts/runner/registrar.sh`: instala el runner de GitHub Actions en `/opt/actions-runner` como servicio, con un usuario `runner` que pertenece al grupo `docker` y las etiquetas `self-hosted,linux,dsa-dev`. Lo ejecuto yo una vez por Session Manager, porque el token de registro caduca en poco tiempo.
- `scripts/db/crear-bases.sh`, para ejecutarlo por SSM en el EC2 de dev:
  - Crea `dsa_dev` y `dsa_prod`, la extensión `vector` y, por ambiente, un usuario del backend y otro de permisos mínimos para el MCP.
  - Guarda las contraseñas generadas como SecureString en SSM.
- **Listo cuando:** después de reiniciar el lab la app vuelve a levantarse sola, y `deploy.sh` con un tag inexistente regresa a la versión anterior.

## Fase 5: pipelines de despliegue
- `vercel.json` con `"git": { "deploymentEnabled": false }`. El frontend solo se despliega desde Actions, con los secretos `VERCEL_TOKEN`, `VERCEL_ORG_ID` y `VERCEL_PROJECT_ID`.

**`.github/workflows/deploy-dev.yml`** (en `push` a `dev` y `workflow_dispatch`, con `concurrency: deploy-dev`):
1. `build`: matriz `backend` y `mcp` con `docker/build-push-action`; publica en GHCR los tags `<sha>` y `dev`.
2. `deploy-backend`: `runs-on: [self-hosted, dsa-dev]`, `environment: dev` (URL `https://api-dev.<DOMINIO>`); ejecuta `/opt/dsa/deploy.sh <sha> dev`.
3. `deploy-frontend`: `vercel pull`, luego `vercel build` con `VITE_API_URL=https://api-dev.<DOMINIO>`, luego `vercel deploy --prebuilt` y `vercel alias set` hacia `dev.<DOMINIO>`.

**`.github/workflows/deploy-prod.yml`** (en `push` a `main` y `workflow_dispatch` con el input `version` para rollback; `concurrency: deploy-prod` sin cancelar en curso):
1. `verificar`:
   - Checkout con `fetch-depth: 2` y `DEV_SHA=$(git rev-parse HEAD^2)`; si no hay segundo padre, falla.
   - Revisa que existan las imágenes con `docker manifest inspect`.
   - Revisa con `gh api` que el último despliegue al environment `dev` de ese SHA terminó en `success`.
   - Calcula la versión siguiente (patch del último tag `v*`).
2. `promover`: `docker buildx imagetools create` para agregar los tags `<version>` y `prod` a las imágenes de `DEV_SHA`.
3. `deploy-backend`: `runs-on: [self-hosted, dsa-dev]`, `environment: prod`.
   - Ejecuta `aws ssm send-command` con `AWS-RunShellScript` hacia `Key=tag:Env,Values=prod`, corriendo `/opt/dsa/deploy.sh <version> prod`.
   - Espera el resultado y falla si no es `Success`.
4. `deploy-frontend`: checkout de `DEV_SHA`, build con `VITE_API_URL=https://api.<DOMINIO>` y `vercel deploy --prebuilt --prod` (`app.<DOMINIO>`).
5. `release`: `gh release create <version> --target <sha del merge> --generate-notes`.
6. **Rollback:** con `workflow_dispatch` y una `version` existente, salta `verificar` y `promover` y despliega esa versión.

**Seguridad del runner:** ningún workflow que use `self-hosted` se dispara con `pull_request`. Permisos mínimos por workflow (`contents: read`, `packages: write` solo en build y `deployments: write` donde haga falta).

- **Listo cuando:** un push a `dev` despliega solo; un PR de `dev` a `main` con merge commit despliega a prod la misma imagen; el rollback funciona.

## Fase 6: documentación
- `docs/ci-cd/runbook.md`:
  - Encender el lab y verificar la salud.
  - Cargar las credenciales del lab para Terraform.
  - Relanzar un despliegue que se quedó en cola.
  - Hacer rollback.
  - Renovar la key de Tailscale y volver a registrar el runner.
  - Recrear todo si la cuenta del lab se reinicia, y en qué orden.
  - Activar Cognito (`AUTH_MODE=cognito`).
- `docs/ci-cd/flujo-de-ramas.md`: una página corta para el equipo sobre cómo trabajar con ramas por tarea, PR a `dev` y el paso a `main`.

## Pasos manuales de Juan Pablo
Claude Code no puede hacer estos pasos; solo prepara scripts e instrucciones.
- Comprar el dominio y crear en el registrador los CNAME: validación de ACM, `api` y `api-dev` hacia el ALB, y `app` y `dev` hacia Vercel.
- Pegar las credenciales del lab para Terraform en cada sesión.
- Generar la auth key de Tailscale (reutilizable, no efímera, `tag:aws`), configurar la ACL `tag:aws → tag:gpu:11434` y guardar la key en SSM.
- Registrar el runner self-hosted.
- Crear el proyecto en Vercel y los secretos `VERCEL_*` en GitHub.
- Hacer públicos los paquetes de GHCR después del primer push.
- Revisar y ejecutar `scripts/github/configurar-repo.sh`.
- Verificar en el lab que ACM, Cognito y SSM Run Command funcionan, y qué cobra con el lab apagado.


## Ajustes 2026-11-10 (tienen prioridad sobre las fases de arriba)
Ver también la actualización del mismo día en [[tec/data-steward-agentico/arquitectura/decision-infraestructura-en-learner-lab|infraestructura en Learner Lab]].

**El repo de código ya existe y tiene trabajo del equipo:**
- Antes de crear nada, revisa la estructura real del repo y sus ramas. El frente de datos está en la carpeta `datos/` (paquete `steward_datos`, migraciones `0001` a `0003`, semillas, catálogo de reglas, scripts de evaluación y 227 pruebas con PostgreSQL + pgvector), con documentación en `docs/datos/`, en la rama `datos/fases-0-a-4`.
- No muevas, renombres ni reescribas código de otros integrantes. Ajusta las rutas del CI, los Dockerfiles, el `Makefile` y Compose a la estructura real. Si no coincide con la de esta guía (`backend/`, `mcp/`, `db/migrations/`), propónmelo antes de reorganizar.
- Detecta qué herramienta de migraciones usa el repo y úsala en el `Makefile` y en `deploy.sh`, en lugar de suponer Alembic.
- `.gitattributes`: conserva las reglas existentes (los PDF e imágenes de prueba están marcados como binarios); solo agrega.
- CI: agrega un job para `datos/` que corra sus pruebas con el service container de pgvector.

**Base de datos:**
- Terraform de RDS:
  - `publicly_accessible = var.db_publica` (por defecto `true`) y subnet group con las subredes públicas.
  - Security group con el 5432 abierto desde `var.db_allowed_cidrs` (por defecto `0.0.0.0/0`).
  - Parameter group con `rds.force_ssl = 1`.
  - El cierre del 24 de noviembre debe ser solo cambiar esas dos variables.
- `scripts/db/crear-bases.sh` (con el usuario maestro, **antes** de cualquier migración):
  - Crea `dsa_dev` y `dsa_prod` y la extensión `vector` en ambas.
  - Crea los roles `steward_migraciones` (dueño del esquema), `steward_backend`, `steward_mcp`, `steward_consultas` (con `statement_timeout` de 5 s) y `steward_carga`.
  - Crea los grupos `equipo_lectura` (`SELECT` en ambas bases) y `equipo_datos` (lectura y escritura de datos solo en `dsa_dev`), con permisos por defecto para que las tablas nuevas también queden cubiertas.
  - Crea un usuario por integrante con su grupo.
  - Las contraseñas se generan y se guardan como SecureString en SSM; nunca se imprimen ni van a archivos.
  - Es idempotente: si un rol ya existe, no falla.
- Las migraciones nunca crean roles con contraseña; solo otorgan permisos.
- `deploy.sh` corre las migraciones como `steward_migraciones`, y los contenedores usan `steward_backend`, `steward_mcp` y `steward_consultas`.
- En la primera migración contra RDS dev, revisa si aparece el `WARNING` de la migración `0003` sobre `set_config` y avísame.

**Datos:**
- `make datos` corre las semillas existentes del frente de datos contra la base del `.env`. El mismo comando sirve para dev y prod con `steward_carga`.
- `docs/ci-cd/acceso-base.md`: cómo se conecta el equipo con DBeaver o pgAdmin (`sslmode=require`) y qué puede hacer cada grupo. Sin host ni contraseñas.
- Agrega al runbook el cierre del 24 de noviembre.


## Actualización 2026-11-17
- La versión vigente de esta guía es la **v3**, en el repo de código (`docs/ci-cd/guia-claude-code-v3.md`). Esta nota queda como antecedente.
- Las Fases 0 a 3 ya están hechas, con desviaciones: sin ALB ni ACM (Caddy e IP elástica) y la revisión de code owners no es obligatoria. Ver [[tec/data-steward-agentico/sesiones/2026-11-17-juan-pablo-fases-0-a-3-infra-ci-cd|la sesión]].
