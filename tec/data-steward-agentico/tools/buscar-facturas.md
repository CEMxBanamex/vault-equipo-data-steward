---
tipo: tool
fecha: 2026-11-04
resumen: Lista facturas concretas con filtros predefinidos (proveedor, fechas, resultado, regla).
---
# Tool: buscar_facturas

- **Qué hace:** consulta parametrizada para preguntas que piden ver registros y no una cifra agregada, como "muéstrame las facturas rechazadas del proveedor X".
- **Recibe:** filtros opcionales: proveedor, rango de fechas, resultado, regla que falló; límite y orden.
- **Devuelve:** lista de facturas con folio, proveedor, fecha, total, resultado y enlace al caso.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-analista-de-datos|Analista de datos]]. Segunda opción después de `obtener_metrica`.
- **Implementa:** Iris / Mario.
- **Paso:** "Buscando facturas de …".
- **Reglas:** consulta parametrizada, sin SQL del modelo; respeta los permisos por rol.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Mauricio (antes Iris / Mario), porque lista lo mismo que la bandeja de casos. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].
