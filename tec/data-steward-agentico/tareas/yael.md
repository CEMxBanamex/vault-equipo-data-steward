---
tipo: tareas
fecha: 2026-11-09
autor: yael
resumen: Tareas de Yael (Frontend) por semana y su estado. Solo Yael las marca; juan-pablo agrega las de cada semana.
---
# Tareas de Yael

Frente: Frontend. Estados: `[ ]` pendiente, `[/]` en proceso, `[x]` listo, `[!]` bloqueado (agrega `· bloqueo: <motivo>`). Cambia solo la casilla y, si hace falta, `bloqueo` o `nota`. Formato y reglas: [[tec/data-steward-agentico/tareas/_index|tareas]]. Estado del equipo: [[tec/data-steward-agentico/tareas/_tablero|tablero]].

## Semana 1 · 9 al 13 nov
- [x] **S1-34** División de pantallas con Mauricio, por escrito · vence: 2026-11-10 · apoyo: mauricio · listo cuando: una nota en interfaces/ dice quién hace cada pantalla · nota: sugerencia: Yael casos y bitácora; Mauricio chat, línea de pasos y login
- [x] **S1-35** Base del frontend: Vite + React, rutas, layout y sistema de diseño · vence: 2026-11-10 · apoyo: mauricio · depende: S1-01 · listo cuando: el proyecto corre en local con las rutas de todas las pantallas y los componentes base del mockup
- [x] **S1-36** Stubs de FastAPI de los endpoints de sus pantallas · vence: 2026-11-10 · depende: S1-01, S1-34 · listo cuando: endpoints con modelos de Pydantic y datos fijos, listos para la revisión de contratos
- [x] **S1-37** Primera versión de registrar_hallazgo y consultar_bitacora · vence: 2026-11-13 · depende: S1-06, S1-27 · listo cuando: ambas tools pasan sus pruebas contra la base local · nota: ver la propuesta de Mario sobre estas tools
- [x] **S1-38** Pantallas de casos y bitácora con MSW · vence: 2026-11-13 · depende: S1-06, S1-35 · listo cuando: bandeja, detalle, decisión y bitácora funcionan con datos simulados y los tipos del OpenAPI

## Semana 3 · 23 al 29 nov
- [x] **S3-29** Prompt y pruebas del agente redactor · vence: 2026-11-24 · apoyo: carlos-delgado · listo cuando: cada hallazgo de las 4 facturas de la demo se explica con su regla, versión y evidencia, con pruebas que pasan · nota: Pruebas con las cuatro facturas de demo y sus respaldos, usando extracción de referencia. CI del PR #46: https://github.com/CEMxBanamex/Banamex_Monorepo/actions/runs/45519818962
- [x] **S3-30** Endpoints reales de casos y bitácora · vence: 2026-11-24 · apoyo: carlos-delgado · depende: S3-11 · listo cuando: los 6 endpoints llaman a procesar_caso, reanudar_caso y a la base, sin datos fijos · nota: Integrado en dev mediante el PR #46: https://github.com/CEMxBanamex/Banamex_Monorepo/pull/46
- [ ] **S3-31** Pantallas de casos y bitácora sin MSW en dev · vence: 2026-11-24 · depende: S3-30, S3-04 · listo cuando: en dev.cem-steward.online se sube una factura, se ve el detalle con sus hallazgos, se decide y la decisión aparece en la bitácora
- [x] **S3-32** Prueba de punta a punta del flujo de casos · vence: 2026-11-28 · depende: S3-31 · listo cuando: una prueba automatizada de subir, revisar, decidir y ver la bitácora pasa en local o en el CI · nota: Pasó test_casos_e2e en el CI del PR #46 con grafo, base de pruebas y servicios controlados: https://github.com/CEMxBanamex/Banamex_Monorepo/actions/runs/45519818962
