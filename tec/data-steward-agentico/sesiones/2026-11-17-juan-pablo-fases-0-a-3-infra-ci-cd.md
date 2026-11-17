---
tipo: sesion
fecha: 2026-11-17
autor: juan-pablo
resumen: Fases 0 a 3 de infraestructura y CI/CD en el repo de código (11 y 12 nov.) - reorganización, entorno local, CI con reglas del repo y Terraform sin ALB, verificado y sin aplicar.
---
# Sesión 2026-11-11 y 12: fases 0 a 3 de infraestructura y CI/CD

Trabajo con Claude Code en el repo de código siguiendo la guía v3 (`docs/ci-cd/guia-claude-code-v3.md`, versión más nueva que [[tec/data-steward-agentico/arquitectura/guia-claude-code-ci-cd|la guía del vault]]). Una fase a la vez, cada una por PR hacia `dev`. La nota se escribió el 17 de noviembre.

## Qué se hizo
| Fase | Qué quedó en `dev` | PR del repo de código |
|---|---|---|
| 0 · Reorganización | Rama `dev` creada desde `main`. Las dos ramas de Carlos Delgado integradas. Migraciones y semillas movidas a `db/`; el servidor MCP a `mcp/steward_mcp/` y el grafo de casos a `backend/grafo_casos/` | 3 a 6 |
| 1 · Entorno local | `docker-compose.dev.yml` (PostgreSQL + pgvector, S3 local, backend y mcp), Dockerfiles, SQL de roles en `db/roles/`, `Makefile`, `.env.example` y `/api/health` | 7 |
| 2 · CI y reglas del repo | `ci.yml` con `ci-ok` como único check obligatorio, Dependabot, `CODEOWNERS`, plantilla de PR y script de reglas, ya aplicado | 8 |
| 3 · Terraform | `infra/terraform/` con `bootstrap`, `envs/shared`, `envs/dev`, `envs/prod` y 8 módulos. **Nada aplicado en AWS** | 10 |

**Cómo se verificó:**
- Fases 0 y 1: las pruebas de datos pasan igual que antes de mover nada (245 con la base local, sin ninguna saltada). Pasan también las del MCP, el grafo y backend. `make up && make migrate && make datos` funciona desde una copia limpia.
- Fase 2: el CI corrió en verde en su primer PR. Un PR de prueba hacia `main` desde otra rama quedó bloqueado por el job `origen-main`.
- Fase 3: `terraform validate` pasa en las cuatro raíces y no hay recursos de IAM. Con el lab encendido, el `plan` de `shared` dio 31 recursos por crear, sin errores. Se confirmó en la cuenta que `db.t4g.micro` con PostgreSQL 16.15 y `t3.small` están disponibles, y que existe `LabInstanceProfile`.
- En la Fase 3, dos subagentes escribieron los módulos de Terraform y Claude Code definió las interfaces, integró y revisó todo.

## Decisiones
Las de infraestructura están como actualización del 2026-11-17 en [[tec/data-steward-agentico/arquitectura/decision-infraestructura-en-learner-lab|infraestructura en Learner Lab]]; las de ramas y CI, en [[tec/data-steward-agentico/arquitectura/decision-ramas-y-ci-cd|ramas y CI/CD]]. En resumen:
- **Sin ALB ni ACM.** Quedaban menos de 30 USD de créditos y el ALB cobra todo el tiempo. El HTTPS lo da Caddy en cada EC2, con una IP elástica.
- **API abierta a internet** mientras `AUTH_MODE=dev`, porque el equipo cambia de red e IP. Se cierra con Cognito.
- **Reorganización intermedia del repo:** `steward_datos` se queda en `datos/`; los imports se unificaron a `steward_datos`.
- **`CODEOWNERS` solo sugiere revisores:** `main` pide una aprobación de cualquier integrante.

## Aprendizajes
- **`set_config` en la seguridad por fila:** el `REVOKE` de la migración `0003` no tiene efecto si quien migra no es dueño de la función. Ahora lo hace `db/roles/02_base.sql` como superusuario. En RDS el usuario maestro tampoco es dueño, así que puede seguir sin aplicar.
- **La carpeta `mcp/` choca con el SDK `mcp`** de Python. Por eso el paquete del servidor se llama `steward_mcp` y la carpeta no se importa.
- **Lab apagado:** las credenciales siguen respondiendo a `aws sts get-caller-identity`, pero las lecturas de EC2 dan `UnauthorizedOperation`. Esa es la señal de que el lab está apagado, no `ExpiredToken`.
- **Lo que cobra con el lab apagado:** las IP elásticas, los discos y el secreto de RDS. El ALB cobraba siempre.
- **`gh` 2.45 falla en `gh pr edit`** por la API de Projects classic. Para cambiar la base de un PR se usa la API REST.

## Pendientes
- **Aplicar Terraform** (desde el 17 nov.): `bootstrap` → `shared` → `dev`, revisando cada plan. `prod` se aplica hasta la Fase 5.
- **Pasos manuales después de aplicar:** registros A de `api-dev` y `api` en el registrador, valores de SSM con la CLI y confirmar la suscripción a las alertas de gasto.
- **Confirmar al aplicar:** que el lab permita la contraseña maestra de RDS en Secrets Manager y AWS Budgets.
- **Para la Fase 4:**
  - Las imágenes no incluyen `db/`, que hace falta para las migraciones en `deploy.sh`.
  - `make datos` no se puede repetir; para recargar hay que usar `make reset-db`.
  - Revisar `set_config` en RDS.
  - Conectar el `user_data` de las EC2.
- **CI:** mypy reporta 78 errores en el código del equipo; por ahora no bloquea.
- **Fase 5:** el repo tiene conectada la integración de Vercel por Git; hay que desactivarla.
- **Lucid:** actualizar el diagrama (sin ALB, Caddy e IP elástica).
- **Tareas:** marcar S1-01 a S1-04 en mi archivo de tareas.

## Siguiente paso
Encender el lab, aplicar `bootstrap`, `shared` y `dev`, y empezar la Fase 4 (Compose de despliegue con Caddy, `user-data.sh`, `deploy.sh`, el script de bases y el del runner).

## Actualización 2026-11-17
- S1-01 a S1-04 quedaron marcadas como listas en [[tec/data-steward-agentico/tareas/juan-pablo|mis tareas]]. S1-05 sigue pendiente hasta aplicar Terraform. S1-10 se hará con GHCR en lugar de ECR, en la Fase 5.
