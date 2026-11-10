---
tipo: tareas
fecha: 2026-11-09
autor: iris
resumen: Tareas de Iris (Datos) por semana y su estado. Solo Iris las marca; juan-pablo agrega las de cada semana.
---
# Tareas de Iris

Frente: Datos. Estados: `[ ]` pendiente, `[/]` en proceso, `[x]` listo, `[!]` bloqueado (agrega `· bloqueo: <motivo>`). Cambia solo la casilla y, si hace falta, `bloqueo` o `nota`. Formato y reglas: [[tec/data-steward-agentico/tareas/_index|tareas]]. Estado del equipo: [[tec/data-steward-agentico/tareas/_tablero|tablero]].

## Semana 1 · 9 al 13 nov
- [x] **S1-12** Catálogo de reglas y casos de referencia · vence: 2026-11-09 · listo cuando: catálogo y casos en la rama datos/fases-0-a-4
- [x] **S1-13** Datos del piloto: 74 facturas y 10 archivos de registros con resultado esperado · vence: 2026-11-09 · apoyo: mario · listo cuando: datos y scripts de evaluación en la rama datos/fases-0-a-4
- [x] **S1-14** validar_reglas y consultar_calidad con pruebas · vence: 2026-11-09 · listo cuando: ambas tools pasan sus pruebas con PostgreSQL + pgvector
- [x] **S1-15** Agente validador: prompt y pruebas · vence: 2026-11-13 · apoyo: carlos-delgado · listo cuando: prompt en el repo y casos de prueba con resultado esperado que pasan
- [x] **S1-16** Descargar FATURA y correr el convertidor · vence: 2026-11-11 · apoyo: carlos-delgado · listo cuando: las facturas de FATURA quedan en el formato del piloto y Carlos Delgado las puede usar en su evaluación de visión · nota: 100 facturas (2 por plantilla) en fatura_piloto_100.zip, entregado a Carlos Delgado; el convertidor ya guarda el valor sin etiqueta (PR #2 del monorepo)
- [x] **S1-17** Políticas de facturas para el RAG · vence: 2026-11-13 · apoyo: mario · listo cuando: las políticas sintéticas de facturas están cargadas y buscar_politicas las encuentra con tipo facturas · nota: 4 políticas tipo facturas (P-001 a P-004, P-002 con dos versiones) en datos/politicas del monorepo; las carga cargar_semilla.py
