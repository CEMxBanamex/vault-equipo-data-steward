---
tipo: tool
fecha: 2026-11-04
resumen: Devuelve las reglas de calidad de una tabla y sus últimos resultados.
---
# Tool: consultar_calidad

- **Qué hace:** consulta las reglas de calidad registradas para una tabla y el resultado de su última ejecución.
- **Recibe:** nombre de tabla y, opcionalmente, dimensión de calidad (completitud, unicidad, validez, oportunidad).
- **Devuelve:** por regla: descripción, dimensión, umbral, último resultado (porcentaje que cumple) y fecha de ejecución.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-de-gobernanza|Agente de gobernanza]].
- **Implementa:** Iris / Mario.
- **Paso:** "Revisando reglas de calidad…".
- **Reglas:** en el piloto los resultados son sintéticos y precargados; no ejecuta las reglas en vivo.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Iris (antes Iris / Mario), porque ella define las reglas de calidad. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].


## Actualización 2026-11-09 (implementación)
- **Estado:** lista, con pruebas. Código: `datos/steward_datos/tools/consultar_calidad.py`.
- **Recibe:** `tabla` (acepta `facturas`, `v_facturas` o "tabla de facturas") y `dimension` opcional (completitud, unicidad, validez, oportunidad, consistencia).
- **Devuelve:** por regla, descripción, dimensión, umbral, último porcentaje, el anterior, si cumple el umbral, registros evaluados y fecha. Si la tabla no tiene reglas, `tablas_con_reglas` para que el agente lo diga.
- **Reglas del piloto:** 13 (RC-001 a RC-013) en `datos/gobernanza/calidad.yaml`, con la política P-022. En facturas, 3 de 5 no alcanzan su umbral (folio completo, folio único y total consistente): sirve para la demo del agente de gobernanza.
- **Paso:** "Revisando reglas de calidad de facturas…".
