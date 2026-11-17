---
tipo: sesion
fecha: 2026-11-10
autor: juan-pablo
resumen: Plan de infraestructura y CI/CD ajustado a AWS Learner Lab - dominio propio, frontend en Vercel, EC2 sin NAT, imágenes en GHCR, runner self-hosted y ramas tarea → dev → main.
---
# Sesión 2026-11-10: infraestructura y CI/CD

## Qué se hizo
- Se analizó la arquitectura propuesta y se ajustó a la cuenta de **AWS Learner Lab** (sesiones de 4 horas, sin roles de IAM ni OIDC, créditos limitados) y a la fecha de cierre de noviembre.
- Se definieron los ambientes (local, dev y prod), la infraestructura en AWS y los pipelines de GitHub Actions.
- Se escribió una guía por fases para que Claude Code implemente todo en el repo de código.

## Decisiones
- [[tec/data-steward-agentico/arquitectura/decision-infraestructura-en-learner-lab|Infraestructura del MVP en AWS Learner Lab]]: dominio propio fuera de AWS, frontend en Vercel, EC2 en subred pública sin NAT, un ALB y una RDS compartidos, SSM Parameter Store, Tailscale para las GPUs.
- [[tec/data-steward-agentico/arquitectura/decision-ramas-y-ci-cd|Ramas y CI/CD del repo de código]]: ramas por tarea → `dev` (sin aprobación, despliega a dev) → `main` (1 aprobación, promueve la misma imagen a prod), imágenes en GHCR y runner self-hosted.
- Guía: [[tec/data-steward-agentico/arquitectura/guia-claude-code-ci-cd|Guía para Claude Code: infraestructura y CI/CD]].

## Aprendizajes
- Learner Lab no permite OIDC ni roles, y sus credenciales caducan: GitHub Actions no puede autenticarse en AWS. Por eso las imágenes van a GHCR y el despliegue lo hace un runner dentro del EC2.
- ngrok resuelve la entrada a un servicio, no la salida a internet de una instancia privada.
- Si el frontend está en un dominio HTTPS (Vercel), la API también necesita HTTPS, o el navegador bloquea las llamadas.
- Cuando el CI filtra jobs por rutas, conviene un job final (`ci-ok`) como único check obligatorio.
- Para que prod encuentre la imagen probada en dev, el PR de `dev` a `main` debe ser merge commit (el squash cambia el SHA).

## Pendientes
- Comprar el dominio.
- Verificar en el lab: ACM, Cognito, SSM Run Command con `LabRole`, qué cobra con el lab apagado y el comportamiento de un ASG.
- Crear el repo de código y arrancar la Fase 1 de la guía con Claude Code.
- Actualizar el diagrama de Lucid (sin Nginx, frontend en Vercel, EC2 en subred pública, un ALB compartido, GHCR).
- Cargar las tareas de infraestructura y CI/CD en el archivo de tareas de juan-pablo.

## Siguiente paso
Copiar la guía al repo de código y pedirle a Claude Code las Fases 1 y 2.


## Actualización 2026-11-10 (acceso a la base y revisión de los cambios del frente de datos)
- **Decidido:** RDS pública temporal hasta el 24 de noviembre, usuarios por persona y por grupo, datos con `make datos`, trabajo diario en local y ventanas de integración para dev. Ver la actualización en [[tec/data-steward-agentico/arquitectura/decision-infraestructura-en-learner-lab|infraestructura en Learner Lab]].
- **Revisión de las sesiones de Iris y Mario del 2026-11-09**, y cómo afectan al plan:
  - El repo de código ya existe, con el frente de datos en `datos/` (rama `datos/fases-0-a-4`). La guía de Claude Code ahora le pide adaptarse a esa estructura y no reorganizar código de otros.
  - Las migraciones esperan los usuarios `steward_backend`, `steward_mcp` y `steward_consultas`; se adoptan esos nombres y se agregan `steward_migraciones` y `steward_carga`.
  - Con una sola RDS para dev y prod, los roles se comparten entre las dos bases.
  - En RDS el `REVOKE` de `set_config` puede no aplicar; hay que verificarlo en la primera migración.
- **Pendientes nuevos:**
  - Decidir si la estructura del monorepo sigue la de la guía o se adapta a `datos/`.
  - Confirmar qué herramienta de migraciones usa el repo.
  - Responder la [[tec/data-steward-agentico/tools/propuesta-vistas-para-consulta-libre-mario|propuesta de Mario]] sobre la lista blanca de funciones en `ejecutar_consulta`.
  - Integrar la rama `datos/fases-0-a-4` a `dev` cuando exista.
