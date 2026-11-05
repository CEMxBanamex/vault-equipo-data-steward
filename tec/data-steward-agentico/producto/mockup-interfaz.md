---
tipo: aprendizaje
fecha: 2026-10-28
resumen: Qué muestra cada pantalla del mockup navegable (Vite + React, sin conexiones), qué se puede hacer en ella y qué principio del producto refleja.
---
# Mockup navegable de la interfaz

Prototipo para enseñar al socio formador cómo va quedando la interfaz. Vive en `frontend/` del repo, es solo UI (sin backend, sin login real, sin subir archivos) y todos los datos son ficticios. Se levanta con `npm run dev` dentro de `frontend/`.

## Pantallas
| # | Pantalla | Qué muestra | Qué se puede hacer |
|---|---|---|---|
| 1 | Inicio de sesión | Marca, propuesta de valor y botón único de entrada; aviso de sesión expirada como variante | Entrar a la bandeja |
| 2 | Bandeja de casos | Contadores por estado, filtros, tabla de casos con estado y resultado sugerido | Buscar por ID o archivo, abrir un caso, ir a subir caso |
| 3 | Subir caso | Tipo de revisión (factura o políticas), zona de arrastre, lista de archivos con progreso y errores, texto pegado | Elegir tipo, agregar o quitar archivos, reintentar una subida fallida, iniciar revisión |
| 4 | Detalle de factura | Documento original con zoom y páginas, datos extraídos con confianza de lectura, hallazgos con regla, versión y evidencia, resultado sugerido | Seleccionar un hallazgo para resaltarlo en el documento, corregir la fecha, escalar, confirmar con diálogo |
| 5 | Detalle de validación con políticas | Registros con celdas problemáticas resaltadas, hallazgo con filas afectadas, políticas consultadas con versión y vigencia | Escalar, confirmar con diálogo |
| 6 | Bitácora | Eventos de personas y del agente, con regla y versión; solo lectura | Expandir un evento para ver valor anterior y nuevo |

## Estados alternos
Un botón **Pantallas** (esquina inferior izquierda) salta directo a cada variante para la demo:
- Bandeja vacía, cargando (esqueleto) y error al cargar.
- Subir caso: tipo no admitido, archivo de más de 20 MB y subida fallida (ya aparecen en la lista inicial).
- Detalle: procesando (pasos que avanzan solos), sin hallazgos, falta evidencia o política, y error de procesamiento.
- Iniciar una revisión de factura lleva al estado procesando y al terminar muestra el detalle.

## Cómo refleja los principios del producto
- **La persona decide:** el resultado es "sugerido" y la acción principal es "Confirmar resultado", con diálogo que recuerda que no autoriza pagos ni operaciones.
- **Verificable:** cada hallazgo muestra regla, versión y evidencia, y al seleccionarlo se resalta la zona en el documento.
- **Incertidumbre explícita:** los campos con menos de 80 % de confianza se marcan como *Dudoso*.
- **Trazabilidad:** cada corrección, escalamiento o confirmación sube el contador de la bitácora; la corrección deja el valor anterior tachado.

## Diseño
Paleta: azul profundo `#003847` (barra, botón principal, títulos), rojo `#FF1A44` solo en el símbolo, estados en verde, rojo, ámbar, azul y neutro. Tipografía Inter con cifras tabulares. Botones de al menos 44 px y foco visible.

- **Enlaces:** [[tec/data-steward-agentico/producto/_index|producto]], [[tec/data-steward-agentico/sesiones/2026-10-28-mockup-interfaz|sesión 2026-10-28]]

## Actualización 2026-10-28 (tarde)
- **Logo:** se reemplazó la aproximación en SVG por el símbolo oficial que pasó JP. Vive en `frontend/src/assets/logo.png`: PNG con fondo transparente, recortado y de 512 px, generado a partir de la imagen original (cuyo fondo era exactamente el azul de marca `#003847`). Se usa en la barra superior y en el panel del inicio de sesión.
- **Deploy:** el mockup está publicado en https://banamex-cem.vercel.app/. Detalles en [[tec/data-steward-agentico/producto/deploy-mockup-vercel|deploy del mockup en Vercel]].
