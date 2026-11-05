---
tipo: tool
fecha: 2026-11-04
resumen: Devuelve la ficha de catálogo de una tabla o columna: descripción, dueño, clasificación de sensibilidad y origen.
---
# Tool: consultar_catalogo

- **Qué hace:** consulta las tablas del catálogo de datos.
- **Recibe:** nombre de tabla y, opcionalmente, de columna.
- **Devuelve:** descripción, dueño (data owner) y responsable (data steward), clasificación de sensibilidad, origen del dato y tablas relacionadas.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-de-gobernanza|Agente de gobernanza]].
- **Implementa:** Iris / Mario.
- **Paso:** "Consultando el catálogo de datos…".
- **Reglas:** devuelve metadatos, nunca los datos mismos.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Juan Pablo (antes Iris / Mario), porque la clasificación de sensibilidad se conecta con la seguridad de las consultas. El contenido del catálogo lo llenan Iris y Mario. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
