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
- [ ] **S1-22** Calibrar el RAG y evaluar el agente de gobernanza con los modelos reales · vence: 2026-11-13 · depende: S1-29 · listo cuando: evaluar_rag.py --calibrar y evaluar_gobernanza.py corren con los modelos de las laptops y el umbral queda fijado
- [ ] **S1-23** Conectar el agente de gobernanza al grafo del chat · vence: 2026-11-13 · apoyo: carlos-ramos · depende: S1-33 · listo cuando: una pregunta de gobernanza en el chat llega a su agente y responde con fuente
