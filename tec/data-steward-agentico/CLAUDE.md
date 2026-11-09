---
tipo: proyecto
fecha: 2026-10-21
resumen: MVP de Data Steward Agéntico para un reto del Tec con un banco como socio formador: agentes LangGraph con tools por MCP que revisan facturas y registros contra políticas, explican cada recomendación y dejan la decisión a una persona.
---
# data-steward-agentico

## Resumen
Reto del Tec con un banco como socio formador (el nombre se omite en el vault). Construimos un MVP de **Data Steward Agéntico**: un sistema multiagente que ayuda a analistas a revisar facturas y registros contra reglas y políticas internas.
Cada recomendación muestra la evidencia, la regla aplicada y su versión, y queda en una bitácora de auditoría. **El agente recomienda y la persona decide:** no hay ninguna tool para liberar pagos.
Backend en FastAPI + LangGraph, tools en un servidor MCP, frontend en Vite + React, todo en AWS (ALB + ASG + EC2 con Docker Compose, RDS PostgreSQL con pgvector, S3, Cognito). La inferencia corre con Ollama en las 5 laptops con GPU del equipo, conectadas por Tailscale.

## Estado actual y siguiente paso
- **Estado (2026-10-21):** arquitectura diseñada y diagrama en Lucid (el enlace está en el README del repo). Ya existe el `README.md` con la solución y la arquitectura, y la imagen del diagrama en `resources/images/arquitectura.webp`. **Falta hacer commit** de ambos. Siguen como *Propuesto*: Nginx, Docker Compose con tres contenedores, ASG en 2 zonas (mín. 1, máx. 3) y Secrets Manager. Todavía no hay código.
- **Siguiente paso:** confirmar los componentes propuestos, registrar la VRAM de cada GPU para asignar modelos por rol y probar el modelo de visión con facturas de FATURA.

## Mapa de áreas
- [[tec/data-steward-agentico/producto/_index|producto]]: historias de usuario, principios, clasificación de resultados, datos del piloto y cómo se mide el éxito.
- [[tec/data-steward-agentico/arquitectura/_index|arquitectura]]: infraestructura en AWS, contenedores, red y seguridad.
- [[tec/data-steward-agentico/agentes/_index|agentes]]: grafo de LangGraph, tools del MCP, flujo de un caso, checkpoints, RAG y bitácora.
- [[tec/data-steward-agentico/modelos/_index|modelos]]: Ollama en las GPUs, reparto por rol, embeddings y la LSTM auxiliar.

## Sesiones
- [[tec/data-steward-agentico/sesiones/2026-10-21-inicio|2026-10-21 inicio]]

## Referencias compartidas
- [[tec/_compartido/ollama-gpus-por-tailscale|Ollama en laptops del equipo vía Tailscale]]: cómo usar las GPUs del equipo como servidores de inferencia desde la nube.

## Repositorio
- `<REPO>`: monorepo en GitHub, rama principal `main`. El nombre se omite porque incluye al socio formador.
- El `README.md` del repo es la referencia completa de la solución y la arquitectura.

## Actualización 2026-10-28
- Área nueva en el mapa: [[tec/data-steward-agentico/interfaces/_index|interfaces]]: mockup de las pantallas del MVP, estados, sistema de diseño y supuestos.
- Sesión nueva: [[tec/data-steward-agentico/sesiones/2026-10-28-mockup-interfaces|2026-10-28 mockup de interfaces]].


## Actualización 2026-10-28 (chat y plan de trabajo)
- **Cambio de alcance:** se quitó la LSTM; se agregan un chat de facturas y los pasos del agente visibles.
- Áreas nuevas en el mapa:
  - [[tec/data-steward-agentico/chat/_index|chat]]: alcance, enrutador por intención, tools de solo lectura y pasos del agente visibles.
  - [[tec/data-steward-agentico/plan-de-trabajo/_index|plan-de-trabajo]]: integrantes del Equipo 1, reparto por frentes, fases y contratos.
- Sesión nueva: [[tec/data-steward-agentico/sesiones/2026-10-28-chat-y-plan-de-trabajo|2026-10-28 chat y plan de trabajo]].
- **Siguiente paso:** arrancar la Fase 0 (entorno local, esquema, prueba de visión y borradores de contratos).


## Actualización 2026-11-04 (agentes y tools)
- Área nueva: [[tec/data-steward-agentico/tools/_index|tools]], una nota por cada una de las 14 tools del MCP (borrador del contrato de sus firmas).
- Notas nuevas en [[tec/data-steward-agentico/agentes/_index|agentes]]: una por cada uno de los 7 agentes (3 del grafo de casos y 4 del chat).
- Sesión: [[tec/data-steward-agentico/sesiones/2026-11-04-agentes-y-tools-del-chat|2026-11-04 agentes y tools del chat]].


## Actualización 2026-11-04 (proyecto compartido con el equipo)
- Este proyecto se comparte con el Equipo 1 en un repo de la organización. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo|Decisión: vault compartido del equipo]].
- Cuando trabajes aquí, aplican también las reglas del `CLAUDE.md` del repo del equipo:
  - Solo los dueños editan notas existentes de su área; fuera de ella, notas `propuesta-<tema>-<rama>.md`.
  - Sesiones nuevas como `sesiones/AAAA-MM-DD-<rama>-<tema>.md`.
  - No editar la sección automática de los `_index.md`.
  - Campo `autor` (nombre de rama) en el frontmatter de notas nuevas.


## Actualización 2026-11-09 (novedades)
- Al empezar, lee [[tec/data-steward-agentico/novedades|novedades]]: lista los últimos 20 cambios que llegaron a `main`, agrupados por fecha y PR, con liga a cada nota y su resumen. Si una novedad toca lo que te piden, abre la nota enlazada antes de responder.
- `novedades.md` lo genera GitHub Actions en cada cambio a `main`; nadie lo edita a mano.
