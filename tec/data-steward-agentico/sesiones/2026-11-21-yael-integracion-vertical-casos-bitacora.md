---
tipo: sesion
fecha: 2026-11-21
autor: yael
resumen: Integración vertical de pantallas de Casos y Bitácora con la API/MSW, subida dinámica de casos, registro de decisión humana y sincronización de dev.
---
# Sesión 2026-11-21 · Integración vertical de Casos y Bitácora

- **Participante:** Yael García (@yaelgl)
- **Frente:** Frontend & Bitácora (Rebanada vertical de Casos)

## Objetivos cumplidos
1. **Conexión dinámica de Bandeja y Bitácora con `api.js`:**
   - Se actualizó `Bandeja.jsx` para consumir `obtenerCasos()` con soporte de estados de carga (`loading`), error con banner interactivo, estado vacío y filtros dinámicos por estado, tipo y resultado.
   - Se actualizó `Bitacora.jsx` para consumir `obtenerBitacora()`, con filtros interactivos por caso y tipo de acción, y detalle expandible de filas.
2. **Subida dinámica de Casos (`Subir.jsx`):**
   - Se conectó el botón «Iniciar revisión» con `crearCaso()` de `api.js`, enviando el archivo y tipo a `POST /api/casos` y navegando directamente al nuevo caso generado.
3. **Decisión del Analista y Auditoría Inmutable (`Detalle.jsx` y `Validacion.jsx`):**
   - Al confirmar o escalar un caso en la interfaz, se invoca `registrarDecisionCaso()` (`POST /api/casos/{id}/decision`).
   - El endpoint actualiza el estado del caso en memoria (`revisado`) e inserta de inmediato el evento correspondiente en `EVENTOS_MOCK` de la bitácora con iniciales del analista y sello de tiempo.
4. **Sincronización con `dev`:**
   - Se integraron limpiamente los cambios recientes de `dev` (despliegue en EC2/RDS de Juan Pablo y calibración de RAG de Mario/Iris) en la rama `frontend/stubs-bitacora-msw-yael`.
5. **Verificación de Pruebas y Compilación:**
   - `npm run build` en `frontend/` compilado en 2.39s sin errores.
   - `pytest tests/test_api_stubs.py` (5/5 pasadas).
   - `pytest tests/test_tools_yael.py` (2/2 pasadas).
   - Pruebas del grafo de casos y redactor en `backend/grafo_casos/tests/` (5/5 pasadas).
   - Commit `7f33251` subido a GitHub en la rama `frontend/stubs-bitacora-msw-yael`.
