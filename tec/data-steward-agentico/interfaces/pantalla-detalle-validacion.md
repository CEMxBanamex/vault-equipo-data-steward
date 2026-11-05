---
tipo: pantalla
fecha: 2026-10-28
resumen: Pantalla 5, como el detalle de factura pero con los registros en tabla, filas con problema resaltadas y la lista de políticas consultadas.
---
# Pantalla 5: detalle de validación con políticas

Misma estructura, acciones y estados que el [[tec/data-steward-agentico/interfaces/pantalla-detalle-factura|detalle de factura]].

## Izquierda
Tabla tipo Excel de `clientes_octubre.xlsx` (120 registros). Las filas con problema se marcan y la celda vacía lleva borde de advertencia.

## Derecha
- **Hallazgo:** "Campo obligatorio faltante: `correo_contacto`". 8 de 120 registros. Filas 14, 27, 33, 48, 61, 79, 95 y 112. Regla P-007, versión 1.3.
- **Políticas consultadas:** nombre, versión y vigencia (P-007, más P-011 y P-015 como ejemplo).
- **Resultado sugerido:** Rechazado. Es un supuesto: el brief no lo define.

← [[tec/data-steward-agentico/interfaces/_index|interfaces]]
