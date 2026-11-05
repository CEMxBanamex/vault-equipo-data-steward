---
tipo: tool
fecha: 2026-11-04
resumen: Devuelve las reglas de calidad de una tabla y sus últimos resultados.
---
# Tool: consultar_calidad

- **Qué hace:** consulta las reglas de calidad registradas para una tabla y el resultado de su última ejecución.
- **Recibe:** nombre de tabla y, opcionalmente, dimensión de calidad (completitud, unicidad, validez, oportunidad).
- **Devuelve:** por regla: descripción, dimensión, umbral, último resultado (porcentaje que cumple) y fecha de ejecución.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-de-gobernanza|Agente de gobernanza]].
- **Implementa:** Iris / Mario.
- **Paso:** "Revisando reglas de calidad…".
- **Reglas:** en el piloto los resultados son sintéticos y precargados; no ejecuta las reglas en vivo.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Iris (antes Iris / Mario), porque ella define las reglas de calidad. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
