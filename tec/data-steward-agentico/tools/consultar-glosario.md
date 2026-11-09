---
tipo: tool
fecha: 2026-11-04
resumen: Devuelve la definición oficial de un término de negocio desde el glosario.
---
# Tool: consultar_glosario

- **Qué hace:** busca un término en el glosario de negocio (coincidencia exacta y luego aproximada).
- **Recibe:** término.
- **Devuelve:** definición, sinónimos, dueño del término y términos relacionados; si no existe, lo indica.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-de-gobernanza|Agente de gobernanza]].
- **Implementa:** Iris / Mario.
- **Paso:** "Consultando el glosario…".
- **Reglas:** si el término no está, el agente lo dice en lugar de inventar una definición.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Mario (antes Iris / Mario), porque él define el glosario. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].


## Actualización 2026-11-09 (implementación)
- **Estado:** lista, con pruebas. Código: `datos/steward_datos/tools/consultar_glosario.py`. Términos en `datos/gobernanza/glosario.yaml` (tabla legible en `docs/datos/glosario.md`).
- **Glosario:** 32 términos de facturas, proveedores, pagos, presupuesto, clientes, auditoría y gobernanza (por ejemplo, factura conciliada, monto facturado, data owner, dato personal, regla de calidad), cada uno con dueño (política P-021) y fuente.
- **Búsqueda:** exacta, luego por sinónimo ("OC" → Orden de compra, "dueño de los datos" → Data owner) y al final aproximada. Si nada se parece lo suficiente, `encontrado` es falso y devuelve alternativas: el agente dice que el término no está, sin inventarlo.
- **Devuelve:** `coincidencia` (`exacta`, `sinonimo` o `aproximada`), definición, sinónimos, dominio, dueño, términos relacionados y fuente.
