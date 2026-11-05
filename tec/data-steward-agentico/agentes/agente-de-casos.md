---
tipo: agente
fecha: 2026-11-04
resumen: Agente del chat que explica un caso concreto (datos, hallazgos, reglas y decisión) y responde preguntas de auditoría con la bitácora.
---
# Agente: Casos

- **Grafo:** chat. Lo llama el [[tec/data-steward-agentico/agentes/agente-enrutador|Enrutador]]. En el panel dentro de un caso, el `caso_id` ya viene en el contexto.
- **Ejemplos:** "¿Por qué se rechazó?", "¿Qué regla falló y qué versión?", "¿De dónde sacaste el subtotal?", "¿Quién tomó la decisión y cuándo?".
- **Tools:** [[tec/data-steward-agentico/tools/consultar-caso|consultar_caso]], [[tec/data-steward-agentico/tools/consultar-bitacora|consultar_bitacora]].
- **Regla clave:** solo lectura; explica lo que ya decidieron el validador y el analista, no cambia el resultado.
- **Construye:** Carlos Delgado / Carlos Ramos (las tools, Iris y Mario).
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]]


## Actualización 2026-11-04 (subequipo)
- **Subequipo:** grafo del chat, liderado por Carlos Ramos.
- **Dueño:** Mauricio (prompt, pruebas y evaluación). **Apoyo:** Yael.
- **Tools y sus responsables:** `consultar_caso` (Mauricio), `consultar_bitacora` (Yael).
- Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|subequipos de agentes]].
