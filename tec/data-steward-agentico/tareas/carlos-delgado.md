---
tipo: tareas
fecha: 2026-11-09
autor: carlos-delgado
resumen: Tareas de Carlos Delgado (Agentes y modelos) por semana y su estado. Solo Carlos Delgado las marca; juan-pablo agrega las de cada semana.
---
# Tareas de Carlos Delgado

Frente: Agentes y modelos. Estados: `[ ]` pendiente, `[/]` en proceso, `[x]` listo, `[!]` bloqueado (agrega `· bloqueo: <motivo>`). Cambia solo la casilla y, si hace falta, `bloqueo` o `nota`. Formato y reglas: [[tec/data-steward-agentico/tareas/_index|tareas]]. Estado del equipo: [[tec/data-steward-agentico/tareas/_tablero|tablero]].

## Semana 1 · 9 al 13 nov
- [x] **S1-24** Modelo de embeddings: embeddinggemma:300m · vence: 2026-11-09 · listo cuando: decisión documentada en modelos/
- [x] **S1-25** Registrar la VRAM de cada GPU · vence: 2026-11-10 · apoyo: todos · listo cuando: tabla con la VRAM de las 5 laptops en modelos/ y un reparto de modelos por rol propuesto
- [/] **S1-26** Evaluación controlada del modelo de visión y decisión: local o Bedrock · vence: 2026-11-11 · depende: S1-16 · listo cuando: mismo prompt y configuración sobre al menos 20 facturas, precisión por campo y la decisión documentada · nota: gemma3:4b es el candidato provisional
- [ ] **S1-27** Servidor MCP base y tool de ejemplo con la convención · vence: 2026-11-12 · apoyo: carlos-ramos · depende: S1-06 · listo cuando: el MCP corre en local con una tool de ejemplo que maneja rol, errores, pasos y pruebas, documentada para copiarla
- [ ] **S1-28** Esqueleto del grafo de casos con tools falsas · vence: 2026-11-13 · depende: S1-27 · listo cuando: procesar_caso recorre extractor, validador y redactor con tools falsas y se pausa para la decisión del analista
