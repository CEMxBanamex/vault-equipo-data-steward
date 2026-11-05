---
tipo: sesion
fecha: 2026-10-28
resumen: Se construyó el mockup navegable de la interfaz en Vite + React a partir de las 11 pantallas de diseño, solo UI y con datos ficticios, para enseñarlo al socio formador.
---
# Sesión 2026-10-28: mockup de la interfaz

## Qué se hizo
- Se recibieron 11 imágenes de diseño: inicio de sesión (normal y sesión expirada), bandeja, subir caso, detalle de factura (normal, diálogo de confirmar y campo corregido), validación con políticas, bitácora, variantes de estado y paleta de componentes.
- Se creó `frontend/` en el repo con Vite + React (y `lucide-react` para íconos). Es solo interfaz: no hay llamadas a API, autenticación ni subida real.
- La navegación funciona con botones entre las seis pantallas, y un menú **Pantallas** salta a cada estado alterno.
- Se documentó cada pantalla en [[tec/data-steward-agentico/producto/mockup-interfaz|Mockup navegable de la interfaz]].

## Decisiones
- Navegación con estado de React en lugar de un enrutador, porque el mockup no necesita URLs y así se evita una dependencia.
- Los casos de la bandeja abren la variante que les corresponde (F-1041 sin hallazgos, V-0206 error, V-0207 validación).

## Pendientes
- Hacer commit de `frontend/` y de `.claude/launch.json` en el repo.
- Recoger la retroalimentación del socio sobre el mockup.
- Cuando se conecte con el backend: sustituir `src/data.js` por llamadas a FastAPI y el login simulado por Cognito.

## Siguiente paso
Enseñar el mockup al socio formador y ajustar según sus comentarios.

## Actualización 2026-10-28 (tarde)
- Se cambió el logo por el símbolo oficial (PNG transparente en `frontend/src/assets/logo.png`).
- El código ya estaba en GitHub y al día. No aparecía en Vercel porque el repo es de la organización y no de la cuenta personal.
- JP hizo el deploy en Vercel con Root Directory `frontend`: https://banamex-cem.vercel.app/. Ver [[tec/data-steward-agentico/producto/deploy-mockup-vercel|deploy del mockup en Vercel]].
- Pendientes que se cierran: commit de `frontend/` (ya estaba en `main`).
- Pendientes nuevos: hacer commit del cambio de logo para que Vercel lo despliegue, y decidir si se activa Deployment Protection, porque la URL es pública.
- Siguiente paso: compartir la URL con el socio formador y recoger su retroalimentación.
- Corrección: el cambio de logo ya estaba en `main` (el repo no tenía cambios pendientes), así que ese pendiente queda cerrado.
