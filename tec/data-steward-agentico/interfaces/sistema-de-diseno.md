---
tipo: referencia
fecha: 2026-10-28
resumen: Paleta en hex, tipografía, componentes reutilizables para React y reglas de accesibilidad del mockup.
---
# Sistema de diseño

## Paleta
| Uso | Texto o color | Fondo |
|---|---|---|
| Marca, azul profundo (barra superior, botón principal, títulos) | #003847 | — |
| Marca, rojo (solo el símbolo; nunca para estados) | #FF1A44 | — |
| Éxito · Aceptado | #11663D | #E6F4EC |
| Error · Rechazado | #A8201A | #FCEBEA |
| Advertencia · revisión humana, dudoso | #8A5300 (borde #D99A1E) | #FFF3D6 |
| Información · Procesando | #0B57A4 | #E5EFFA |
| Neutral · regla, versión, evidencia | #44555E | #EDF1F3 |
| Texto principal / secundario | #12232B / #51636C | — |
| Fondo de la app / bordes | #F4F6F7 / #DDE4E7 | — |
| Foco con teclado | #2E8BC0 | — |

Los dos colores de marca se extrajeron del logo del socio formador.

## Tipografía
Inter. Título 28, bloque 17, cuerpo 15, etiqueta 13. Números en tablas con `font-variant-numeric: tabular-nums`.

## Componentes (para React)
- `Badge`: estado y resultado, siempre con ícono y texto.
- `DataTable`: filtros, orden y filas clicables.
- `FindingCard`: título, explicación, regla, versión y evidencia.
- `ConfidenceField`: input, barra de confianza y badge "Dudoso".
- `FileDropzone` y `UploadItem` con progreso.
- `ConfirmDialog`, `Toast`, `Banner`, `Skeleton`, `EmptyState`.

## Reglas
- Botones de al menos 44 px de alto; una sola acción principal por pantalla.
- Contraste AA y foco visible.
- Íconos de línea; esquinas de 8 a 12 px.

← [[tec/data-steward-agentico/interfaces/_index|interfaces]]
