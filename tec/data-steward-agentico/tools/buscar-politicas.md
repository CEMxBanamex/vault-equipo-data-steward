---
tipo: tool
fecha: 2026-11-04
resumen: Búsqueda semántica en el RAG (pgvector) de políticas de facturas o de gobernanza, con fuente, versión y vigencia de cada fragmento.
---
# Tool: buscar_politicas

- **Qué hace:** genera el embedding de la consulta y busca los fragmentos más cercanos en pgvector, filtrando por tipo y vigencia.
- **Recibe:** texto de la consulta, tipo (`facturas` o `gobernanza`) y número máximo de fragmentos.
- **Devuelve:** fragmentos con documento fuente, versión, vigencia y puntaje de similitud.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-validador|Validador]] y [[tec/data-steward-agentico/agentes/agente-de-gobernanza|Agente de gobernanza]]. Es la única tool compartida.
- **Implementa:** Iris / Mario.
- **Paso:** "Buscando política de …".
- **Reglas:** el mismo modelo de embeddings al indexar y al consultar. Ver [[tec/data-steward-agentico/modelos/mismo-modelo-de-embeddings|aprendizaje]]. Solo políticas vigentes salvo que se pida una versión.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Carlos Delgado / Carlos Ramos (antes Iris / Mario), porque depende del modelo de embeddings. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
