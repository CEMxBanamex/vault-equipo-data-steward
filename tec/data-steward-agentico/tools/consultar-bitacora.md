---
tipo: tool
fecha: 2026-11-04
resumen: Consulta la bitácora de auditoría con filtros: quién hizo qué, sobre qué caso y cuándo.
---
# Tool: consultar_bitacora

- **Qué hace:** lee los eventos de la bitácora para responder preguntas de auditoría, como "¿quién aprobó la F-1042?" o "¿qué decisiones se tomaron ayer?".
- **Recibe:** filtros opcionales: `caso_id`, usuario, tipo de evento, rango de fechas; límite.
- **Devuelve:** eventos con fecha, usuario, acción, caso y detalle.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-de-casos|Agente de casos]].
- **Implementa:** Iris / Mario.
- **Paso:** "Revisando la bitácora…".
- **Reglas:** solo lectura; respeta los permisos por rol.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Yael (antes Iris / Mario), porque lee la misma bitácora que muestra su pantalla. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
