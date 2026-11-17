---
tipo: decision
fecha: 2026-11-10
autor: juan-pablo
resumen: Repo de código con ramas por tarea → dev → main; push a dev despliega al EC2 de dev y fusionar dev a main promueve a prod la misma imagen ya probada, con CI en cada PR, imágenes en GHCR y un runner self-hosted.
---
# Decisión: ramas y CI/CD del repo de código

- **Contexto:** el equipo quiere un ambiente de integración (dev) y uno de producción (prod), y que prod solo reciba lo que ya pasó por dev. AWS es Learner Lab, así que GitHub no puede guardar credenciales de AWS (caducan y no se permite OIDC). Ver [[tec/data-steward-agentico/arquitectura/decision-infraestructura-en-learner-lab|infraestructura en Learner Lab]].
- **Decisión:** ver las secciones de abajo.
- **Por qué:** cada rama dice a dónde va su código; prod corre exactamente la imagen probada en dev; nadie se bloquea esperando revisión para integrar, y el único punto de control es el paso a prod.
- **Enlaces:** [[tec/data-steward-agentico/arquitectura/_index|arquitectura]], [[tec/data-steward-agentico/arquitectura/guia-claude-code-ci-cd|Guía para Claude Code]]

## Ramas
| Rama | Para qué | Qué pasa al recibir cambios |
|---|---|---|
| `<nombre>/<tarea>` (ej. `jp/infra-rds`, `yael/chat-sse`) | Trabajo de cada quien, se prueba en local | CI cuando abren PR hacia `dev` |
| `dev` | Integración del equipo | Build, imágenes a GHCR y despliegue automático al EC2 de dev |
| `main` | Producción | Verifica que viene de dev y promueve la misma imagen al EC2 de prod |

- Ramas cortas **por tarea**, con el nombre de la persona como prefijo. No ramas permanentes por persona: en el código todos tocan los mismos archivos y las ramas largas terminan en conflictos grandes.
- **Todo pasa por `dev`, incluso los arreglos urgentes.** Rama de arreglo → PR a `dev` → se verifica en dev → PR de `dev` a `main`. Un PR directo a `main` lo bloquea el CI.

## Protección de ramas
**`dev`:**
- PR obligatorio, **sin aprobaciones**.
- Checks de CI obligatorios (son lo único que evita que alguien rompa dev para todos).
- La rama debe estar al día con `dev` antes de fusionar.
- Solo squash merge; sin force push.

**`main`:**
- PR obligatorio y solo desde `dev` (check `origen-main`).
- **1 aprobación** de alguien distinto al autor, de un responsable de entregas (`CODEOWNERS` + "requerir revisión de code owners").
- Se descartan aprobaciones viejas si llegan commits nuevos.
- Checks de CI obligatorios.
- **Solo merge commit** (no squash): así el pipeline encuentra el SHA de dev que se fusionó.
- Sin force push.

El environment `prod` de GitHub no pide una segunda aprobación: el PR a `main` ya es el punto de control. Se puede activar si hace falta controlar la hora exacta del despliegue.

## Pipelines
**`ci.yml`** (PR hacia `dev` o `main`, y push a `dev`):
- Filtro por rutas para correr solo lo que cambió.
- `backend` y `mcp`: ruff, mypy y pytest con Postgres + pgvector.
- `frontend`: eslint, tsc, vitest y build.
- `contracts`: regenera los tipos de TypeScript desde el OpenAPI y falla si hay diferencias.
- `docker-build`: build sin publicar.
- `secrets`: gitleaks. Además, Dependabot semanal hacia `dev`.
- `origen-main`: en PR a `main`, falla si la rama de origen no es `dev`.
- `ci-ok`: un job final que junta a los demás; es el único check obligatorio, para que los jobs saltados por el filtro no bloqueen.

**`deploy-dev.yml`** (push a `dev`):
1. Runners de GitHub construyen `backend` y `mcp` y los publican en GHCR con el SHA del commit.
2. El runner self-hosted del EC2 de dev ejecuta `deploy.sh`: migraciones con Alembic, `docker compose pull`, `up -d` y health check; si falla, regresa a la imagen anterior.
3. Despliega el frontend en Vercel y lo asigna a `dev.<dominio>`.
4. El job usa el environment `dev`, así GitHub registra que ese SHA se desplegó bien.

**`deploy-prod.yml`** (push a `main`):
1. Obtiene el SHA de dev que se fusionó (segundo padre del merge, `HEAD^2`); si no hay merge commit, falla.
2. Verifica que existan en GHCR las imágenes de ese SHA y que su despliegue a dev haya terminado bien.
3. Re-etiqueta esas imágenes con la versión (`vX.Y.Z`); no se reconstruye nada.
4. El runner del EC2 de dev ejecuta `deploy.sh` en las instancias con etiqueta `Env=prod` por SSM Run Command.
5. Despliega el frontend a producción en Vercel (`app.<dominio>`).
6. Crea el tag y el release con notas generadas.
- **Rollback:** el mismo workflow a mano (`workflow_dispatch`) con la versión anterior.

## Runner self-hosted
- Vive en el EC2 de dev y usa `LabInstanceProfile`: no hay llaves de AWS en GitHub.
- Si el lab está apagado, el despliegue queda en cola hasta que se encienda; si pasa mucho tiempo, se relanza a mano.
- Como el repo es público, el runner **solo** corre en push a `dev` y `main` y en `workflow_dispatch`, **nunca** en `pull_request`, y con un usuario sin privilegios de administrador.
- Las dos instancias viven en el mismo lab, así que se encienden y se apagan juntas.

## Por qué GHCR
- Se autentica con el `GITHUB_TOKEN`; no hace falta guardar credenciales de AWS que caducan.
- Las imágenes quedan fuera de la cuenta del lab.
- El build corre aunque el lab esté apagado y no le quita CPU al EC2.
- Prod usa exactamente la imagen probada en dev.
- Paquetes públicos: el EC2 los baja sin token. Las imágenes nunca llevan secretos ni datos.

## Alternativas descartadas
- **Solo `main` con tags para prod:** más simple, pero el equipo prefiere que el nombre de la rama indique el ambiente.
- **Ramas permanentes por persona:** conflictos grandes al integrar.
- **Hotfix directo a `main`:** rompe la garantía de que prod corre lo probado en dev y desincroniza las ramas.
- **Aprobación obligatoria en `dev`:** frena la integración con 7 personas y 3 semanas.
- **Construir en el EC2 o subir a ECR desde el runner:** builds lentos en una instancia chica, solo con el lab encendido.


## Actualización 2026-11-17 (implementado)
Sesión: [[tec/data-steward-agentico/sesiones/2026-11-17-juan-pablo-fases-0-a-3-infra-ci-cd|fases 0 a 3]].

- **Ya existen en el repo de código:** la rama `dev`, el CI (`ci.yml`) y las reglas de `dev` y `main`. Se verificó que un PR hacia `main` desde otra rama queda bloqueado.
- **Revisión de code owners: no es obligatoria.** El equipo edita carpetas de otros y no se quería frenar los PR. `CODEOWNERS` solo sugiere a quién pedir revisión; `main` pide una aprobación de cualquier integrante. Para exigirla, basta cambiar un valor en `scripts/github/configurar-repo.sh` y volver a correrlo.
- **Jobs del CI:** `changes`, `python`, `frontend`, `contracts`, `docker-build`, `secrets`, `origen-main` y `ci-ok`.
  - `mypy` es informativo por ahora (78 errores en el código existente).
  - El frontend corre `npm ci` y `vite build`; eslint, TypeScript y vitest se activan solos cuando existan los scripts `lint`, `typecheck` y `test`.
  - `contracts` se activa cuando exista `contracts/openapi.json`.
- **Otras reglas aplicadas:**
  - Se exige aprobar los workflows de colaboradores externos, por el runner self-hosted y el repo público.
  - Se desactivó el rebase merge.
  - Existen los environments `dev` y `prod`.
- **Ramas:** se usan con el formato `<área>/<tema>-<nombre>` (por ejemplo `infra/terraform-juan-pablo`), que reemplaza al `<nombre>/<tarea>` de arriba.
