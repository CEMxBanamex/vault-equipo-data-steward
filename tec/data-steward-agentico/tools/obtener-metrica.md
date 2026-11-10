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


## Actualización 2026-11-09 (implementación)
- **Estado:** lista, con pruebas. Código en el repo de código: `datos/steward_datos/tools/obtener_metrica.py`. Definiciones en `datos/semantica/metricas.yaml` (tabla legible en `docs/datos/metricas.md`).
- **Métricas (12):** `monto_facturado`, `numero_facturas`, `facturas_rechazadas`, `tasa_rechazo`, `tasa_conciliacion`, `tiempo_promedio_revision`, `facturas_por_regla`, `casos_pendientes`, `monto_pagado`, `pagos_a_tiempo`, `monto_comprometido` y `clientes_activos`.
- **Recibe (`ObtenerMetricaEntrada`):** `metrica`, hasta 2 `dimensiones` (proveedor, mes, entidad, centro_costo, moneda, resultado, regla…, según la métrica), `filtros`, `fecha_desde`, `fecha_hasta`, `orden` y `limite`.
- **Devuelve:** filas, definición oficial (el agente la cita), unidad, el SQL generado con sus parámetros (para el detalle del paso) y `truncado`. Si la pregunta no encaja, devuelve `MetricaNoDisponible` con las métricas disponibles y una sugerencia; el agente pasa a `buscar_facturas` o a la consulta libre.
- **Seguridad:** el SQL lo arma el código solo con piezas del YAML; los valores del usuario van como parámetros. Lee de las vistas con el rol y el usuario del JWT (los fija el servidor MCP con `steward_datos.contexto.usuario_actual`), así que la seguridad por fila aplica. Sin contexto, falla.
- **Paso:** "Calculando monto facturado por proveedor…".
