---
tipo: referencia
fecha: 2026-11-09
autor: juan-pablo
resumen: Diagrama en Lucidchart de los 7 agentes (grafo de casos y grafo del chat) y las 14 tools del MCP que usa cada uno.
---
# Diagrama: agentes y tools

- **Liga:** [Data Steward Agéntico - Agentes y tools (Lucidchart)](https://lucid.app/lucidchart/3f031a66-937d-4d2d-954c-943b81c15d7a/edit)
- **Qué muestra:** tres franjas.
  - **Arriba, grafo de casos:** Extractor → Validador → Redactor → revisión humana (`interrupt`).
  - **En medio, servidor MCP:** las 14 tools, con un color por grupo (documentos, validación, gobernanza, consultas y casos).
  - **Abajo, grafo del chat:** el Enrutador reparte a Gobernanza, Analista de datos y Casos, más las salidas de respuesta general y fuera de alcance.
- **Detalles:**
  - `buscar_politicas` (en amarillo) es la única tool compartida entre los dos grafos.
  - Los números 1, 2, 3a y 3b marcan el orden de decisión del Analista de datos.
  - Ninguna tool libera pagos ni cambia el resultado de un caso.
- **Fuente:** las notas de [[tec/data-steward-agentico/agentes/_index|agentes]] y [[tec/data-steward-agentico/tools/_index|tools]], con el reparto vigente del 2026-11-04.
- **Acceso:** la liga no incluye invitación; pide acceso a Juan Pablo si Lucid no te deja abrirlo.
