---
tipo: tareas
fecha: 2026-11-09
autor: carlos-ramos
resumen: Tareas de Carlos Ramos (Agentes y modelos) por semana y su estado. Solo Carlos Ramos las marca; juan-pablo agrega las de cada semana.
---
# Tareas de Carlos Ramos

Frente: Agentes y modelos. Estados: `[ ]` pendiente, `[/]` en proceso, `[x]` listo, `[!]` bloqueado (agrega `· bloqueo: <motivo>`). Cambia solo la casilla y, si hace falta, `bloqueo` o `nota`. Formato y reglas: [[tec/data-steward-agentico/tareas/_index|tareas]]. Estado del equipo: [[tec/data-steward-agentico/tareas/_tablero|tablero]].

## Semana 1 · 9 al 13 nov
- [x] **S1-29** Ollama expuesto por Tailscale desde una laptop · vence: 2026-11-10 · apoyo: juan-pablo · listo cuando: otra máquina del tailnet llama a Ollama en el puerto 11434 y no es accesible fuera de Tailscale
- [x] **S1-30** Borrador de los eventos SSE del chat · vence: 2026-11-10 · apoyo: mauricio · listo cuando: modelos de Pydantic de los eventos en contratos/ con una secuencia de ejemplo
- [x] **S1-31** Prueba rápida de text-to-SQL con el modelo local · vence: 2026-11-11 · listo cuando: 10 preguntas sobre las vistas de Mario, con el SQL generado y cuántas salieron correctas
- [x] **S1-32** Agente de ejemplo con la convención · vence: 2026-11-12 · apoyo: carlos-delgado · depende: S1-06 · listo cuando: un agente con prompt, manejo de errores, pasos y pruebas, documentado para copiarlo
- [x] **S1-33** Esqueleto del grafo del chat con tools falsas · vence: 2026-11-13 · depende: S1-32 · listo cuando: stream_chat enruta por dominio, incluida la intención mixta, con tools falsas y emite los eventos SSE

## Semana 3 · 23 al 29 nov
- [ ] **S3-14** Laptop de demo sirviendo los tres modelos por Tailscale · vence: 2026-11-23 · apoyo: juan-pablo · listo cuando: una sola URL de Ollama sirve gemma3:4b, embeddinggemma:300m y el modelo de chat, y responde desde dsa-dev · nota: si no cabe en la VRAM, el modelo de chat va en una segunda laptop y se avisa a juan-pablo para usar una URL por rol
- [ ] **S3-15** Grafo del chat mínimo para la demo (cierra S1-33) · vence: 2026-11-24 · apoyo: mario, mauricio · listo cuando: stream_chat enruta a gobernanza, casos, general y fuera de alcance con tools reales y emite los eventos SSE del contrato · nota: sin intención mixta; corte a las 17:00 del martes, antes del ensayo de las 20:00
- [ ] **S3-16** Agente analista de datos · vence: 2026-11-27 · apoyo: mario, mauricio, juan-pablo · depende: S3-15, S1-08 · listo cuando: responde 10 preguntas de negocio con obtener_metrica, buscar_facturas o la consulta libre, y muestra la métrica o el SQL en los pasos
- [ ] **S3-17** Intención mixta · vence: 2026-11-28 · depende: S3-16 · listo cuando: una pregunta que combina dos dominios llama a ambos agentes y la respuesta cita las fuentes de los dos · nota: opcional; se recorta si no alcanza
- [ ] **S3-18** Evaluación del enrutador · vence: 2026-11-28 · apoyo: mario · depende: S3-15 · listo cuando: 30 preguntas etiquetadas por dominio y el porcentaje de aciertos documentado
