---
tipo: decision
fecha: 2026-10-21
resumen: Sumas, campos obligatorios y formatos se comprueban con código determinista en la tool validar_reglas; el LLM extrae, busca y explica, pero no calcula.
---
# Decisión: las validaciones exactas las hace el código, no el LLM

- **Contexto:** la Historia 1 depende de comprobaciones exactas (por ejemplo, que subtotal más impuestos sea igual al total). Un LLM puede equivocarse en aritmética o dar resultados distintos en cada corrida.
- **Decisión:** la tool `validar_reglas` del MCP hace las comprobaciones exactas en código: sumas, campos obligatorios y formatos. El LLM extrae los datos, recupera las políticas y redacta la explicación.
- **Por qué:** el resultado es reproducible y auditable: la misma factura da siempre el mismo dictamen, y la explicación puede citar la regla y la diferencia exacta.
- **Alternativas descartadas:** pedirle al LLM que revise las sumas.
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]], [[tec/data-steward-agentico/producto/_index|producto]]
