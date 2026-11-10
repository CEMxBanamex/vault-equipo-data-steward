---
tipo: tareas
fecha: 2026-11-09
autor: yael
resumen: Tareas de Yael (Frontend) por semana y su estado. Solo Yael las marca; juan-pablo agrega las de cada semana.
---
# Tareas de Yael

Frente: Frontend. Estados: `[ ]` pendiente, `[/]` en proceso, `[x]` listo, `[!]` bloqueado (agrega `· bloqueo: <motivo>`). Cambia solo la casilla y, si hace falta, `bloqueo` o `nota`. Formato y reglas: [[tec/data-steward-agentico/tareas/_index|tareas]]. Estado del equipo: [[tec/data-steward-agentico/tareas/_tablero|tablero]].

## Semana 1 · 9 al 13 nov
- [ ] **S1-34** División de pantallas con Mauricio, por escrito · vence: 2026-11-10 · apoyo: mauricio · listo cuando: una nota en interfaces/ dice quién hace cada pantalla · nota: sugerencia: Yael casos y bitácora; Mauricio chat, línea de pasos y login
- [ ] **S1-35** Base del frontend: Vite + React, rutas, layout y sistema de diseño · vence: 2026-11-10 · apoyo: mauricio · depende: S1-01 · listo cuando: el proyecto corre en local con las rutas de todas las pantallas y los componentes base del mockup
- [ ] **S1-36** Stubs de FastAPI de los endpoints de sus pantallas · vence: 2026-11-10 · depende: S1-01, S1-34 · listo cuando: endpoints con modelos de Pydantic y datos fijos, listos para la revisión de contratos
- [ ] **S1-37** Primera versión de registrar_hallazgo y consultar_bitacora · vence: 2026-11-13 · depende: S1-06, S1-27 · listo cuando: ambas tools pasan sus pruebas contra la base local · nota: ver la propuesta de Mario sobre estas tools
- [ ] **S1-38** Pantallas de casos y bitácora con MSW · vence: 2026-11-13 · depende: S1-06, S1-35 · listo cuando: bandeja, detalle, decisión y bitácora funcionan con datos simulados y los tipos del OpenAPI
