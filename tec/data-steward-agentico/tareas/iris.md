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

## Semana 3 · 23 al 29 nov
- [ ] **S3-23** Facturas de la demo · vence: 2026-11-23 · apoyo: carlos-delgado · listo cuando: 4 facturas elegidas (una correcta, una con total que no cuadra, una con campo faltante y una con un dato de baja confianza) con su resultado esperado, probadas en local
- [ ] **S3-24** Guion de la demo · vence: 2026-11-24 · apoyo: todos · depende: S3-20, S3-23 · listo cuando: guion de 10 a 12 minutos en el vault con los pasos, quién presenta cada parte, las URLs y el plan B
- [ ] **S3-25** Video de respaldo de la demo · vence: 2026-11-24 · depende: S3-05 · listo cuando: grabación de unos 5 minutos del flujo de facturas y del chat, para usarla si falla el lab el miércoles
- [ ] **S3-26** Regla de la lista 69-B · vence: 2026-11-27 · listo cuando: validar_reglas rechaza un emisor definitivo y manda a revisión uno presunto, con un RFC sintético en una lista de prueba, su política y sus pruebas
- [ ] **S3-27** Prueba de instrucciones inyectadas · vence: 2026-11-28 · apoyo: carlos-delgado · depende: S3-11 · listo cuando: una factura con texto que pide ignorar las reglas no cambia el resultado y queda como caso de evaluación
- [ ] **S3-28** Presentación final y entrega #hito · vence: 2026-11-29 · apoyo: todos · listo cuando: presentación, documentación de entrega y video final listos y revisados por el equipo
