---
tipo: tool
fecha: 2026-11-04
resumen: Muestra al analista de datos las vistas que puede consultar y la descripción de cada columna, antes de escribir SQL de respaldo.
---
# Tool: listar_vistas_consultables

- **Qué hace:** devuelve el esquema de las vistas permitidas para el SQL de respaldo (por ejemplo `v_facturas`, `v_proveedores`, `v_casos`).
- **Recibe:** opcionalmente, el nombre de una vista para ver solo su detalle.
- **Devuelve:** por vista: descripción, columnas con su tipo y descripción, y ejemplos de valores no sensibles.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-analista-de-datos|Analista de datos]], antes de `ejecutar_consulta`.
- **Implementa:** Iris / Mario.
- **Paso:** "Revisando vistas disponibles…".
- **Reglas:** solo muestra las vistas a las que el rol del usuario tiene acceso. Descripciones claras mejoran mucho la precisión del SQL.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Juan Pablo (antes Iris / Mario), porque decide qué vistas son consultables junto con `ejecutar_consulta`. Las vistas las crean Iris y Mario. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
