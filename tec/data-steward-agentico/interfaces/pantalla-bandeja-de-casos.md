---
tipo: pantalla
fecha: 2026-10-28
resumen: Pantalla 2, lista de casos con resumen, filtros y tabla; desde aquí se abre el detalle de cada caso.
---
# Pantalla 2: bandeja de casos

## Contenido
- Título "Casos" y botón principal **Subir caso**.
- Cuatro tarjetas de resumen: Procesando, En revisión, Requieren revisión humana, Revisados hoy.
- Búsqueda por ID o archivo y filtros: estado, tipo de revisión, resultado sugerido y fecha.
- Tabla: ID del caso, archivo, tipo de revisión, estado, resultado sugerido, fecha y responsable. El ID abre el [[tec/data-steward-agentico/interfaces/pantalla-detalle-factura|detalle de factura]] o el [[tec/data-steward-agentico/interfaces/pantalla-detalle-validacion|detalle de validación]].

## Valores
- **Estado:** Procesando · En revisión · Revisado · Error de procesamiento.
- **Resultado sugerido:** Aceptado · Rechazado · Requiere revisión humana (vacío, "—", mientras procesa).

## Estados de pantalla
- Vacío: "Aún no hay casos. Sube tu primer archivo" + botón Subir caso.
- Cargando: esqueleto de la tabla.
- Error al cargar: banner + Reintentar.

## Datos de ejemplo
| ID | Archivo | Tipo | Estado | Resultado |
|---|---|---|---|---|
| F-1042 | factura_1042.pdf | Factura | En revisión | Requiere revisión humana |
| F-1041 | factura_1041.png | Factura | Revisado | Aceptado |
| F-1040 | factura_1040.jpg | Factura | Revisado | Rechazado |
| V-0207 | clientes_octubre.xlsx | Validación con políticas | Procesando | — |
| V-0206 | registros_prueba.csv | Validación con políticas | Error de procesamiento | — |

## Roles
El menú muestra **Políticas** solo al administrador.

← [[tec/data-steward-agentico/interfaces/_index|interfaces]]
