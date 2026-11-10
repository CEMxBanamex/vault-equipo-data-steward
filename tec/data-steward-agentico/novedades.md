---
tipo: novedades
fecha: 2026-11-09
autor: vault-bot
resumen: Los últimos 20 cambios que llegaron a main, con liga a cada nota. Léelo al empezar.
---
# Novedades del vault

_Lo genera GitHub Actions en cada cambio a `main`. No lo edites a mano._

Muestra los últimos 20 cambios, del más reciente al más antiguo. Si una novedad toca lo que te piden, abre la nota enlazada antes de responder. Para cambios más antiguos, consulta el historial de Git de `main`.

## 2026-11-09

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
