---
tipo: propuesta
fecha: 2026-11-09
autor: mario
resumen: Ofrecer a Mauricio las implementaciones de consultar_caso y buscar_facturas y los datos que ya tiene la base para probarlas.
---
# Propuesta: consultar_caso y buscar_facturas

- **Notas que se cambiarían:** [[tec/data-steward-agentico/tools/consultar-caso|consultar_caso]] y [[tec/data-steward-agentico/tools/buscar-facturas|buscar_facturas]] (Mauricio).
- **Qué ya está en el repo de código** (`datos/steward_datos/tools/consultas_chat.py`):
  - **`consultar_caso`:** devuelve estado, resultado sugerido y final, campos con confianza y corrección, hallazgos con regla, versión y evidencia, y los eventos de la bitácora.
  - **`buscar_facturas`:** usa filtros cerrados (proveedor o RFC, folio, fechas, montos, moneda, resultado, estado y regla con hallazgo), sin SQL del modelo. Tiene orden y límite.
- **Datos para probar:** 995 casos.
  - Los 5 de la demo tienen los mismos IDs que el mockup.
  - 30 históricos con archivo.
  - 960 de negocio (`F-0001` a `F-0960`).
- **Qué propongo:**
  - Tomarlas como base, cambiarlas o descartarlas.
  - Si se quedan, leer de `v_casos` y `v_facturas` (que ya filtran por rol y entidad) en lugar de las tablas, para que respeten los permisos por rol como piden sus notas.
- **Por qué:** se construyeron antes del reparto; la decisión es de Mauricio.
- **Estado:** pendiente
