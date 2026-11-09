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


## Actualización 2026-11-09 (Iris)
- **Entrada esperada del Extractor:** `FacturaExtraida` con `valor` tal como está impreso, `confianza` de 0 a 100, `etiqueta` opcional y `texto_completo` (lo usa R-030 para detectar instrucciones inyectadas).
- **Cómo decide el resultado:** lo calcula `validar_reglas`, no el LLM. Si algún hallazgo tiene efecto *revisión* (baja confianza, monto alto, proveedor fuera del padrón, posible duplicado, moneda no admitida, instrucciones inyectadas o documento sin política), el resultado es Requiere revisión humana. Si no, cualquier *rechazo* da Rechazado. Sin hallazgos, Aceptado.
- **Qué hace el LLM del validador:** busca con [[tec/data-steward-agentico/tools/buscar-politicas|buscar_politicas]] (tipo `facturas`, o `gobernanza` en la Historia 2) el fragmento que sustenta cada hallazgo y lo pasa al Redactor con política, versión y sección. No cambia el resultado.
- **Riesgo abierto:** sin confianza por campo del modelo de visión, R-003 no se evalúa. Ver [[tec/data-steward-agentico/modelos/propuesta-confianza-y-evaluacion-vision-iris|propuesta]].
- **Evaluación:** 39 casos de referencia con resultado y reglas esperadas; `scripts/evaluar.py` da la matriz de confusión y los falsos aceptados.
