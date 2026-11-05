---
tipo: tool
fecha: 2026-11-04
resumen: Evalúa en código las reglas del catálogo sobre los campos extraídos y devuelve el resultado de cada regla con su versión y evidencia.
---
# Tool: validar_reglas

- **Qué hace:** aplica las reglas deterministas del catálogo, por ejemplo subtotal + impuestos = total, campos obligatorios presentes y duplicados.
- **Recibe:** campos extraídos del caso y tipo de documento.
- **Devuelve:** lista de resultados por regla: identificador, versión, cumple o no, evidencia y diferencia cuando aplica, más un resultado sugerido (aceptado, rechazado o requiere revisión).
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-validador|Validador]].
- **Implementa:** Iris / Mario.
- **Paso:** "Validando reglas…".
- **Reglas:** el LLM nunca hace estas cuentas. Con pruebas unitarias por regla. Ver [[tec/data-steward-agentico/agentes/decision-validaciones-deterministas-en-codigo|decisión]].
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Iris (antes Iris / Mario), porque ella define el catálogo de reglas. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
