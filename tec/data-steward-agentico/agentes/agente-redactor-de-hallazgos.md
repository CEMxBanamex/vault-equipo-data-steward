---
tipo: agente
fecha: 2026-11-04
resumen: Tercer agente del grafo de casos: explica cada hallazgo con su evidencia, lo registra y deja el caso en pausa para la decisión del analista.
---
# Agente: Redactor de hallazgos

- **Grafo:** procesamiento de casos. Paso 3 de 3.
- **Qué hace:** redacta una explicación clara por hallazgo (qué regla, qué versión, qué evidencia, qué diferencia), propone el resultado sugerido y registra todo en la bitácora. Después el grafo se pausa con `interrupt` hasta que el analista decide.
- **Tools:** [[tec/data-steward-agentico/tools/registrar-hallazgo|registrar_hallazgo]].
- **Modelo:** razonamiento y explicación.
- **Regla clave:** recomienda, no decide; si falta evidencia, marca el caso como "requiere revisión humana".
- **Construye:** Carlos Delgado / Carlos Ramos.
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]]


## Actualización 2026-11-04 (subequipo)
- **Subequipo:** grafo de casos, liderado por Carlos Delgado.
- **Dueño:** Yael (prompt, pruebas y evaluación). **Apoyo:** Carlos Delgado.
- **Tools y sus responsables:** `registrar_hallazgo` (Yael).
- Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|subequipos de agentes]].
