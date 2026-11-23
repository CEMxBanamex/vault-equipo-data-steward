---
tipo: novedades
fecha: 2026-11-23
autor: vault-bot
resumen: Los últimos 20 cambios que llegaron a main, con liga a cada nota. Léelo al empezar.
---
# Novedades del vault

_Lo genera GitHub Actions en cada cambio a `main`. No lo edites a mano._

Muestra los últimos 20 cambios, del más reciente al más antiguo. Si una novedad toca lo que te piden, abre la nota enlazada antes de responder. Para cambios más antiguos, consulta el historial de Git de `main`.

El avance de las tareas no aparece aquí: está en [[tec/data-steward-agentico/tareas/_tablero|el tablero de tareas]].

## 2026-11-23

### docs: sesión del despliegue de dev e infraestructura aplicada · juan-pablo · PR #15
- **Modificada:** [[tec/data-steward-agentico/arquitectura/decision-infraestructura-en-learner-lab|decision-infraestructura-en-learner-lab]]
  Infraestructura del MVP ajustada a AWS Learner Lab y al cierre de noviembre - EC2 de dev y prod detrás de un ALB compartido, RDS con pgvector, S3, SSM, imágenes en GHCR, frontend en Vercel y dominio propio fuera de AWS.
- **Modificada:** [[tec/data-steward-agentico/arquitectura/decision-ramas-y-ci-cd|decision-ramas-y-ci-cd]]
  Repo de código con ramas por tarea → dev → main; push a dev despliega al EC2 de dev y fusionar dev a main promueve a prod la misma imagen ya probada, con CI en cada PR, imágenes en GHCR y un runner self-hosted.
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-22-juan-pablo-despliegue-dev|2026-11-22-juan-pablo-despliegue-dev]]
  Infraestructura de dev aplicada en el Learner Lab y primer despliegue automático completo (backend en EC2 con migraciones, frontend en Vercel), con los arreglos que pidió el lab; S1-05, S1-07 y S1-10 listas.

### docs: supuestos del piloto sin el socio formador · juan-pablo · PR #14
- **Nueva:** [[tec/data-steward-agentico/plan-de-trabajo/decision-supuestos-sin-socio-formador|decision-supuestos-sin-socio-formador]]
  Sin contacto con el socio formador, el piloto adopta como definitivos los supuestos de datos, reglas y gobernanza, y fundamenta las políticas de facturas en normas públicas del SAT (CFF art. 29-A, Anexo 20 y lista 69-B).

## 2026-11-17

### Yael · yael · PR #11
- **Nueva:** [[tec/data-steward-agentico/interfaces/decision-division-de-pantallas|decision-division-de-pantallas]]
  Reparto de pantallas y endpoints del frontend entre Yael (Casos y Bitácora) y Mauricio (Chat, Pasos y Login).
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-17-yael-avance-semana-1|2026-11-17-yael-avance-semana-1]]
  Conexión del vault vía MCP, formalización de división de pantallas, stubs de FastAPI, tools de bitácora y MSW en frontend (100% Semana 1).
- **Modificada:** [[tec/data-steward-agentico/agentes/agente-redactor-de-hallazgos|agente-redactor-de-hallazgos]]
  Tercer agente del grafo de casos: explica cada hallazgo con su evidencia, lo registra y deja el caso en pausa para la decisión del analista.

### JP / S0 - S4 Complete · juan-pablo · PR #10
- **Nueva:** [[tec/data-steward-agentico/arquitectura/decision-infraestructura-en-learner-lab|decision-infraestructura-en-learner-lab]]
  Infraestructura del MVP ajustada a AWS Learner Lab y al cierre de noviembre - EC2 de dev y prod detrás de un ALB compartido, RDS con pgvector, S3, SSM, imágenes en GHCR, frontend en Vercel y dominio propio fuera de AWS.
- **Nueva:** [[tec/data-steward-agentico/arquitectura/decision-ramas-y-ci-cd|decision-ramas-y-ci-cd]]
  Repo de código con ramas por tarea → dev → main; push a dev despliega al EC2 de dev y fusionar dev a main promueve a prod la misma imagen ya probada, con CI en cada PR, imágenes en GHCR y un runner self-hosted.
- **Nueva:** [[tec/data-steward-agentico/arquitectura/guia-claude-code-ci-cd|guia-claude-code-ci-cd]]
  Instrucciones por fases para que Claude Code implemente en el repo de código la infraestructura con Terraform y el CI/CD (ramas, GitHub Actions, despliegue a EC2 y Vercel), con reglas, criterios de terminado y pasos manuales.
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-10-juan-pablo-infraestructura-ci-cd|2026-11-10-juan-pablo-infraestructura-ci-cd]]
  Plan de infraestructura y CI/CD ajustado a AWS Learner Lab - dominio propio, frontend en Vercel, EC2 sin NAT, imágenes en GHCR, runner self-hosted y ramas tarea → dev → main.
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-17-juan-pablo-fases-0-a-3-infra-ci-cd|2026-11-17-juan-pablo-fases-0-a-3-infra-ci-cd]]
  Fases 0 a 3 de infraestructura y CI/CD en el repo de código (11 y 12 nov.) - reorganización, entorno local, CI con reglas del repo y Terraform sin ALB, verificado y sin aplicar.
- **Modificada:** [[tec/data-steward-agentico/arquitectura/_index|_index]]
  Infraestructura del MVP en AWS (ALB, ASG, EC2 con Docker Compose, RDS con pgvector, S3, Cognito), qué está decidido y qué propuesto, contenedores, red y seguridad.

## 2026-11-11

### S1-26: Documentar la evaluación de Gemma 3 para extracción de facturas · carlos-delgado · PR #9
- **Modificada:** [[tec/data-steward-agentico/modelos/decision-modelo-vision-gemma3|decision-modelo-vision-gemma3]]
  Mantener gemma3:4b como candidato de visión para el prototipo y documentar sus resultados y limitaciones.

## 2026-11-10

### Documentar inventario de GPUs y reparto propuesto de modelos · carlos-delgado · PR #8
- **Nueva:** [[tec/data-steward-agentico/modelos/inventario-gpus-y-reparto-modelos|inventario-gpus-y-reparto-modelos]]
  Inventario de las cinco GPUs del equipo y propuesta inicial de reparto para visión, chat, embeddings y respaldo.

### Frente de datos: validar_reglas, consultar_calidad y sesión de configuración · iris · PR #7
- **Nueva:** [[tec/data-steward-agentico/modelos/propuesta-confianza-y-evaluacion-vision-iris|propuesta-confianza-y-evaluacion-vision-iris]]
  Pedir confianza por campo al modelo de visión y medirlo con las facturas sintéticas que ya tienen respuesta esperada.
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-09-iris-configuracion-vault|2026-11-09-iris-configuracion-vault]]
  Configuré Obsidian y Git para trabajar en el vault
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-09-iris-frente-de-datos|2026-11-09-iris-frente-de-datos]]
  Frente de datos con Mario (4 al 9 nov.); de mi parte quedaron validar_reglas, consultar_calidad, las reglas de calidad, el catálogo de reglas y los casos de referencia del piloto.
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-09-iris-validador|2026-11-09-iris-validador]]
  Validador como nodo de código con cita exacta por hallazgo, corrección del filtro de buscar_politicas, R-003 sin confianza y evaluación del validador (39/39).
- **Modificada:** [[tec/data-steward-agentico/agentes/agente-validador|agente-validador]]
  Segundo agente del grafo de casos: corre las reglas deterministas y busca las políticas que las respaldan.
- **Modificada:** [[tec/data-steward-agentico/tools/consultar-calidad|consultar-calidad]]
  Devuelve las reglas de calidad de una tabla y sus últimos resultados.
- **1 notas más** en `tools/`

## 2026-11-09

### feat: tareas por integrante, publicación automática y tablero · juan-pablo · PR #6
- **Nueva:** [[tec/data-steward-agentico/plan-de-trabajo/decision-tareas-por-integrante|decision-tareas-por-integrante]]
  Las tareas viven en un archivo por integrante dentro de tareas/, que solo marca su dueño y se publica en main sin PR; un Action genera el tablero del equipo.
- **Nueva:** [[tec/data-steward-agentico/agentes/diagrama-agentes-y-tools|diagrama-agentes-y-tools]]
  Diagrama en Lucidchart de los 7 agentes (grafo de casos y grafo del chat) y las 14 tools del MCP que usa cada uno.
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-09-juan-pablo-tareas-por-integrante|2026-11-09-juan-pablo-tareas-por-integrante]]
  Plan de la semana 1 (9 al 13 nov.) y sistema de tareas por integrante con publicación automática y tablero generado.
- **Modificada:** [[tec/data-steward-agentico/CLAUDE|CLAUDE]]
  MVP de Data Steward Agéntico para un reto del Tec con un banco como socio formador: agentes LangGraph con tools por MCP que revisan facturas y registros contra políticas, explican cada recomendación y dejan la decisión a una persona.
- **Cambios en el repo:** `.github/CODEOWNERS`, `.github/workflows/sincronizar.yml`, `.gitignore`, `AGENTS.md`, `CLAUDE.md` y 7 más

### Mario · mario · PR #5
- **Nueva:** [[tec/data-steward-agentico/plan-de-trabajo/propuesta-avance-frente-datos-mario|propuesta-avance-frente-datos-mario]]
  Registrar en el plan el avance del frente de datos y los supuestos sobre los datos de negocio.
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-09-mario-frente-de-datos|2026-11-09-mario-frente-de-datos]]
  Frente de datos con Iris (4 al 9 nov.); de mi parte quedaron las vistas con seguridad por fila, los datos de negocio, el catálogo, el glosario, las métricas, las políticas de gobernanza, obtener_metrica y consultar_glosario.
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-09-mario-gobernanza-y-seguridad|2026-11-09-mario-gobernanza-y-seguridad]]
  Prompt y 35 preguntas de prueba del agente de gobernanza, cierre del hueco de set_config en la seguridad por fila y calibración del umbral del RAG.
- **Nueva:** [[tec/data-steward-agentico/tools/propuesta-buscar-politicas-referencia-mario|propuesta-buscar-politicas-referencia-mario]]
  Ofrecer a los Carlos la implementación de buscar_politicas y la ingesta al RAG que ya están en el repo de código, alineadas con embeddinggemma de 768 dimensiones.
- **Nueva:** [[tec/data-steward-agentico/tools/propuesta-consultar-caso-y-buscar-facturas-mario|propuesta-consultar-caso-y-buscar-facturas-mario]]
  Ofrecer a Mauricio las implementaciones de consultar_caso y buscar_facturas y los datos que ya tiene la base para probarlas.
- **Nueva:** [[tec/data-steward-agentico/tools/propuesta-registrar-hallazgo-y-bitacora-mario|propuesta-registrar-hallazgo-y-bitacora-mario]]
  Ofrecer a Yael la implementación de registrar_hallazgo y describir la bitácora de la base para consultar_bitacora.
- **4 notas más** en `agentes/`, `tools/`

### Documentar selección de embeddinggemma:300m · carlos-delgado · PR #2
- **Nueva:** [[tec/data-steward-agentico/modelos/decision-modelo-embeddings-embeddinggemma|decision-modelo-embeddings-embeddinggemma]]
  Seleccionar embeddinggemma:300m para los embeddings del prototipo tras una prueba inicial de recuperación.
- **Nueva:** [[tec/data-steward-agentico/modelos/decision-modelo-vision-gemma3|decision-modelo-vision-gemma3]]
  Mantener gemma3:4b como candidato de visión para el prototipo y documentar sus resultados y limitaciones.

### ci: generar novedades.md en cada cambio a main · juan-pablo · PR #4
- **Modificada:** [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo|decision-vault-compartido-del-equipo]]
  El vault del proyecto se comparte con el equipo en un repo de la organización, con una rama por integrante, PR a main y un Action que regenera índices y propaga main a todas las ramas.
- **Modificada:** [[tec/data-steward-agentico/CLAUDE|CLAUDE]]
  MVP de Data Steward Agéntico para un reto del Tec con un banco como socio formador: agentes LangGraph con tools por MCP que revisan facturas y registros contra políticas, explican cada recomendación y dejan la decisión a una persona.
- **Cambios en el repo:** `.github/workflows/sincronizar.yml`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `README.md` y 1 más

### Juan pablo · juan-pablo · PR #3
- **Modificada:** [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo|decision-vault-compartido-del-equipo]]
  El vault del proyecto se comparte con el equipo en un repo de la organización, con una rama por integrante, PR a main y un Action que regenera índices y propaga main a todas las ramas.
- **Cambios en el repo:** `AGENTS.md`, `GEMINI.md`, `README.md`

## 2026-11-04

### docs: sesión de implementación del repo del equipo · juan-pablo · PR #1
- **Nueva:** [[tec/data-steward-agentico/sesiones/2026-11-04-juan-pablo-implementacion-repo-equipo|2026-11-04-juan-pablo-implementacion-repo-equipo]]
  Implementación del repo compartido del vault: estructura, ramas, token, sincronización, validación de áreas, protección de main y repo público.

### ci: validar que cada integrante solo modifique sus áreas · Juan Pablo Perez · push directo
- **Modificada:** [[tec/data-steward-agentico/plan-de-trabajo/decision-vault-compartido-del-equipo|decision-vault-compartido-del-equipo]]
  El vault del proyecto se comparte con el equipo en un repo de la organización, con una rama por integrante, PR a main y un Action que regenera índices y propaga main a todas las ramas.
- **Cambios en el repo:** `.github/CODEOWNERS`, `.github/integrantes.txt`, `.github/workflows/validar-vault.yml`, `CLAUDE.md`, `scripts/validar_vault.py`

### Full Context and Organization / Juan Pablo · Juan Pablo Perez · push directo
- **Nueva:** [[tec/data-steward-agentico/agentes/decision-checkpoints-y-bitacora-separados|decision-checkpoints-y-bitacora-separados]]
  Los checkpoints de LangGraph son el estado operativo del caso; la bitácora de auditoría es una tabla propia y es el registro oficial.
- **Nueva:** [[tec/data-steward-agentico/agentes/decision-sin-tool-para-liberar-pagos|decision-sin-tool-para-liberar-pagos]]
  El servidor MCP no expone ninguna tool para liberar pagos ni ejecutar operaciones, así que el límite del agente lo impone la arquitectura y no solo el prompt.
- **Nueva:** [[tec/data-steward-agentico/agentes/decision-validaciones-deterministas-en-codigo|decision-validaciones-deterministas-en-codigo]]
  Sumas, campos obligatorios y formatos se comprueban con código determinista en la tool validar_reglas; el LLM extrae, busca y explica, pero no calcula.
- **Nueva:** [[tec/data-steward-agentico/arquitectura/decision-jwt-al-final|decision-jwt-al-final]]
  El login con Cognito por correo se conecta temprano en el frontend, pero la validación del JWT en las APIs se activa al final con un interruptor AUTH_MODE, para probar fácil con Postman.
- **Nueva:** [[tec/data-steward-agentico/arquitectura/decision-monolito-modular|decision-monolito-modular]]
  Un solo repositorio y un solo servicio desplegable, con los agentes como nodos de un grafo LangGraph, porque es lo más simple de desplegar y depurar para un MVP con equipo chico.
- **Nueva:** [[tec/data-steward-agentico/arquitectura/decision-subida-directa-a-s3|decision-subida-directa-a-s3]]
  El navegador sube el archivo del caso directo a S3 con una URL prefirmada, sin pasar por el backend.
- **59 notas más** en `agentes/`, `arquitectura/`, `chat/`, `interfaces/`, `modelos/`, `plan-de-trabajo/`, `producto/`, `sesiones/`, `tec/data-steward-agentico/`, `tools/`
- **Cambios en el repo:** `.gitattributes`, `.github/CODEOWNERS`, `.github/integrantes.txt`, `.github/workflows/sincronizar.yml`, `.github/workflows/validar-vault.yml` y 13 más
