---
tipo: pantalla
fecha: 2026-10-28
resumen: Pantalla 4, la más importante: documento original a la izquierda; datos extraídos, hallazgos y resultado sugerido a la derecha; la persona confirma, corrige o escala.
---
# Pantalla 4: detalle de un caso de factura

## Encabezado
ID (F-1042), archivo, tipo, badge de estado y badge de resultado sugerido.

## Columna izquierda: documento original
- Visor con zoom, "Página 1 de 2" y miniaturas.
- Al seleccionar un hallazgo se resalta su zona en el documento (por ejemplo, el total).

## Columna derecha
1. **Datos extraídos:** proveedor, fecha, subtotal, impuestos, total y moneda. Cada campo es editable y tiene barra de confianza; con menos de 80 % lleva el badge "Dudoso".
2. **Hallazgos:** tarjetas con título, explicación, regla, versión de la regla y evidencia.
3. **Resultado sugerido:** badge, explicación en lenguaje claro y el aviso fijo *"Este resultado indica el cumplimiento de las reglas evaluadas. No autoriza pagos ni operaciones."*

## Barra inferior fija
Comentario opcional · enlace "Bitácora: 4 eventos" · **Corregir dato** · **Escalar caso** · **Confirmar resultado** (única acción principal; abre un diálogo "Quedará registrado en la bitácora").

## Datos de ejemplo
- Proveedor Demo SA · fecha 12/03/2026 (dudosa, 62 %) · subtotal 10,000.00 · impuestos 1,600.00 · total 12,000.00.
- Hallazgo 1: "El total no coincide con subtotal más impuestos". Esperado 11,600.00, encontrado 12,000.00, diferencia 400.00. Regla R-014, versión 2.1, evidencia: página 1, total.
- Hallazgo 2 (agregado en el diseño): "La fecha se leyó con baja confianza". Regla R-003, versión 1.0.
- Resultado sugerido: Requiere revisión humana.

## Estados
- Procesando: pasos "Extrayendo datos", "Consultando reglas", "Validando", "Preparando explicación".
- Con hallazgos (el caso principal).
- Sin hallazgos → Aceptado.
- Falta evidencia o política: "No se encontró una regla aplicable a este caso" → Requiere revisión humana.
- Error de procesamiento, con Reintentar.
- Campo corregido: valor anterior tachado, valor nuevo y "Corregido por [usuario]".

## Para implementar
- La comprobación subtotal + impuestos = total la hace el código, no el LLM ([[tec/data-steward-agentico/agentes/decision-validaciones-deterministas-en-codigo|decisión]]).
- Confirmar, corregir y escalar escriben un evento en la [[tec/data-steward-agentico/interfaces/pantalla-bitacora|bitácora]].

← [[tec/data-steward-agentico/interfaces/_index|interfaces]]
