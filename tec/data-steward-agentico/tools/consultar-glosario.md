---
tipo: tool
fecha: 2026-11-04
resumen: Devuelve la definición oficial de un término de negocio desde el glosario.
---
# Tool: consultar_glosario

- **Qué hace:** busca un término en el glosario de negocio (coincidencia exacta y luego aproximada).
- **Recibe:** término.
- **Devuelve:** definición, sinónimos, dueño del término y términos relacionados; si no existe, lo indica.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-de-gobernanza|Agente de gobernanza]].
- **Implementa:** Iris / Mario.
- **Paso:** "Consultando el glosario…".
- **Reglas:** si el término no está, el agente lo dice en lugar de inventar una definición.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Mario (antes Iris / Mario), porque él define el glosario. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
