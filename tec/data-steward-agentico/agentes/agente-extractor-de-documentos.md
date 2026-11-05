---
tipo: agente
fecha: 2026-11-04
resumen: Primer agente del grafo de casos: lee el archivo y extrae los campos de la factura con el modelo de visión.
---
# Agente: Extractor de documentos

- **Grafo:** procesamiento de casos (pipeline de orden fijo). Paso 1 de 3.
- **Qué hace:** el enrutador por tipo de archivo decide cómo leerlo; luego extrae los campos de la factura con su nivel de confianza.
- **Tools:** [[tec/data-steward-agentico/tools/leer-documento|leer_documento]], [[tec/data-steward-agentico/tools/extraer-campos-factura|extraer_campos_factura]].
- **Entrega al siguiente:** campos extraídos y campos de baja confianza marcados → [[tec/data-steward-agentico/agentes/agente-validador|Validador]].
- **Modelo:** visión, en la laptop asignada a ese rol.
- **Construye:** Carlos Delgado / Carlos Ramos.
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]]


## Actualización 2026-11-04 (subequipo)
- **Subequipo:** grafo de casos, liderado por Carlos Delgado.
- **Dueño:** Carlos Delgado. **Apoyo:** Carlos Ramos.
- **Tools y sus responsables:** `leer_documento` y `extraer_campos_factura` (Carlos Delgado / Carlos Ramos).
- Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|subequipos de agentes]].
