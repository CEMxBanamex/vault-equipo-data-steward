---
tipo: tool
fecha: 2026-11-04
resumen: Calcula una métrica de la capa semántica con dimensiones y filtros; el código genera el SQL, no el modelo.
---
# Tool: obtener_metrica

- **Qué hace:** toma una métrica definida (por ejemplo monto facturado, facturas rechazadas o tiempo promedio de revisión) y la calcula agrupada y filtrada. El SQL lo genera el código a partir de la definición.
- **Recibe:** nombre de la métrica, dimensiones para agrupar (proveedor, mes, regla), filtros y límite.
- **Devuelve:** filas con los valores, la definición oficial de la métrica usada y el SQL generado (para mostrarlo en el paso).
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-analista-de-datos|Analista de datos]]. Es su primera opción.
- **Implementa:** Iris / Mario.
- **Paso:** "Calculando monto facturado por proveedor…", con la métrica como detalle.
- **Reglas:** solo acepta métricas y dimensiones definidas; si no encaja, el agente pasa a `buscar_facturas` o al SQL de respaldo. Las definiciones de métricas son también gobernanza de datos.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]], [[tec/data-steward-agentico/chat/decision-enrutador-por-dominio-y-capa-semantica|decisión]]


## Actualización 2026-11-04
- **Implementa:** Mario (antes Iris / Mario), porque él define las métricas de la capa semántica. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
