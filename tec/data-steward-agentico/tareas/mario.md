---
tipo: tareas
fecha: 2026-11-09
autor: mario
resumen: Tareas de Mario (Datos) por semana y su estado. Solo Mario las marca; juan-pablo agrega las de cada semana.
---
# Tareas de Mario

Frente: Datos. Estados: `[ ]` pendiente, `[/]` en proceso, `[x]` listo, `[!]` bloqueado (agrega `· bloqueo: <motivo>`). Cambia solo la casilla y, si hace falta, `bloqueo` o `nota`. Formato y reglas: [[tec/data-steward-agentico/tareas/_index|tareas]]. Estado del equipo: [[tec/data-steward-agentico/tareas/_tablero|tablero]].

## Semana 1 · 9 al 13 nov
- [x] **S1-18** Esquema, vistas y seguridad por fila (migraciones 0001 a 0003) · vence: 2026-11-09 · apoyo: iris · listo cuando: migraciones en la rama datos/fases-0-a-4 y pruebas en verde
- [x] **S1-19** Datos de negocio sintéticos y contenido de gobernanza · vence: 2026-11-09 · apoyo: iris · listo cuando: 12 meses de datos, catálogo, glosario, 12 métricas y políticas P-020 a P-023 cargados
- [x] **S1-20** obtener_metrica y consultar_glosario con pruebas · vence: 2026-11-09 · listo cuando: ambas tools pasan sus pruebas con PostgreSQL + pgvector
- [x] **S1-21** Prompt y 35 preguntas de prueba del agente de gobernanza · vence: 2026-11-09 · listo cuando: prompt, preguntas y evaluar_gobernanza.py en el repo
- [/] **S1-22** Calibrar el RAG y evaluar el agente de gobernanza con los modelos reales · vence: 2026-11-13 · depende: S1-29 · listo cuando: evaluar_rag.py --calibrar y evaluar_gobernanza.py corren con los modelos de las laptops y el umbral queda fijado · nota: calibrado con embeddinggemma en la laptop de Mario (21 nov.), umbral fijado en 0.37; falta evaluar_gobernanza.py respuestas, que necesita el modelo de chat (S1-31, carlos-ramos)
- [!] **S1-23** Conectar el agente de gobernanza al grafo del chat · vence: 2026-11-13 · apoyo: carlos-ramos · depende: S1-33 · listo cuando: una pregunta de gobernanza en el chat llega a su agente y responde con fuente · bloqueo: el grafo del chat no existe aún; espera S1-33 y S1-32 (carlos-ramos)

## Semana 3 · 23 al 29 nov
- [ ] **S3-19** Agente de gobernanza en el chat para la demo (cierra S1-23) · vence: 2026-11-24 · apoyo: carlos-ramos · depende: S3-15, S3-37 · listo cuando: las preguntas de gobernanza del guion responden en el chat de dev con su fuente
- [ ] **S3-20** Preguntas del chat para la demo · vence: 2026-11-24 · apoyo: mauricio · listo cuando: 8 preguntas (5 de gobernanza y 3 de casos) con su respuesta esperada en el guion de la demo
- [ ] **S3-21** Políticas de facturas con fundamento del SAT · vence: 2026-11-27 · listo cuando: P-001 y P-002 (y P-011 si aplica) citan el CFF art. 29-A y el Anexo 20 como versión nueva, recargadas al RAG, y las preguntas de evaluación del RAG siguen pasando
- [ ] **S3-22** Evaluar las respuestas del agente de gobernanza (cierra S1-22) · vence: 2026-11-27 · depende: S3-14 · listo cuando: evaluar_gobernanza.py corre con el modelo de chat y el resultado queda documentado
