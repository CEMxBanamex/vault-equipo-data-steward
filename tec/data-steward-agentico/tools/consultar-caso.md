---
tipo: tool
fecha: 2026-11-04
resumen: Devuelve todo lo de un caso: datos extraídos, hallazgos con regla y versión, resultado sugerido y decisión del analista.
---
# Tool: consultar_caso

- **Qué hace:** lee de PostgreSQL el estado completo de un caso.
- **Recibe:** `caso_id` (en el chat por caso llega del contexto; en el global, de la pregunta).
- **Devuelve:** datos extraídos con su confianza, hallazgos con regla, versión y evidencia, resultado sugerido, decisión del analista si existe y enlace al original.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-de-casos|Agente de casos]].
- **Implementa:** Iris / Mario.
- **Paso:** "Consultando el caso F-0193…".
- **Reglas:** solo lectura; respeta los permisos por rol.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Mauricio (antes Iris / Mario), porque lee lo mismo que la pantalla de detalle de caso. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
