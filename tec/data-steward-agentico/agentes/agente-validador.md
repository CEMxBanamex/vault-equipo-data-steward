---
tipo: agente
fecha: 2026-11-04
resumen: Segundo agente del grafo de casos: corre las reglas deterministas y busca las políticas que las respaldan.
---
# Agente: Validador

- **Grafo:** procesamiento de casos. Paso 2 de 3.
- **Qué hace:** evalúa las reglas del catálogo sobre los campos extraídos y recupera los fragmentos de política que sustentan cada regla.
- **Tools:** [[tec/data-steward-agentico/tools/validar-reglas|validar_reglas]], [[tec/data-steward-agentico/tools/buscar-politicas|buscar_politicas]] (tipo `facturas`).
- **Entrega al siguiente:** resultados por regla con versión, evidencia y política → [[tec/data-steward-agentico/agentes/agente-redactor-de-hallazgos|Redactor de hallazgos]].
- **Regla clave:** las cuentas y comprobaciones las hace el código, no el LLM.
- **Construye:** Carlos Delgado / Carlos Ramos (las tools, Iris y Mario).
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]]


## Actualización 2026-11-04 (subequipo)
- **Subequipo:** grafo de casos, liderado por Carlos Delgado.
- **Dueño:** Iris (prompt, pruebas y evaluación). **Apoyo:** Carlos Delgado.
- **Tools y sus responsables:** `validar_reglas` (Iris), `buscar_politicas` (Carlos Delgado / Carlos Ramos).
- Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|subequipos de agentes]].
