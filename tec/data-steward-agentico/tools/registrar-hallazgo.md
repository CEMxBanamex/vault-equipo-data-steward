---
tipo: tool
fecha: 2026-11-04
resumen: Escribe un hallazgo en la bitácora de auditoría con su regla, versión, evidencia y explicación.
---
# Tool: registrar_hallazgo

- **Qué hace:** guarda en la bitácora cada hallazgo del caso, separada de los checkpoints de LangGraph.
- **Recibe:** `caso_id`, regla y versión, evidencia, explicación redactada y resultado sugerido.
- **Devuelve:** identificador del registro y su marca de tiempo.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-redactor-de-hallazgos|Redactor de hallazgos]].
- **Implementa:** Iris / Mario.
- **Paso:** "Registrando hallazgos…".
- **Reglas:** solo inserta, nunca modifica ni borra registros. Ver [[tec/data-steward-agentico/agentes/decision-checkpoints-y-bitacora-separados|checkpoints y bitácora separados]].
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Yael (antes Iris / Mario), porque escribe en la misma bitácora que muestra su pantalla. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
