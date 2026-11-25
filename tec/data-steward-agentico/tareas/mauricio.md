---
tipo: tareas
fecha: 2026-11-09
autor: mauricio
resumen: Tareas de Mauricio (Frontend) por semana y su estado. Solo Mauricio las marca; juan-pablo agrega las de cada semana.
---
# Tareas de Mauricio

Frente: Frontend. Estados: `[ ]` pendiente, `[/]` en proceso, `[x]` listo, `[!]` bloqueado (agrega `· bloqueo: <motivo>`). Cambia solo la casilla y, si hace falta, `bloqueo` o `nota`. Formato y reglas: [[tec/data-steward-agentico/tareas/_index|tareas]]. Estado del equipo: [[tec/data-steward-agentico/tareas/_tablero|tablero]].

## Semana 1 · 9 al 13 nov
- [x] **S1-39** Stubs de FastAPI de los endpoints de sus pantallas · vence: 2026-11-10 · depende: S1-01, S1-34 · listo cuando: endpoints con modelos de Pydantic y datos fijos, listos para la revisión de contratos  · 
	nota: PR #18 actualizado con el contrato SSE compartido; comprobaciones de GitHub aprobadas; pendiente de revisión e integración
- [x] **S1-40** Primera versión de consultar_caso y buscar_facturas · vence: 2026-11-13 · depende: S1-06, S1-27 · listo cuando: ambas tools pasan sus pruebas contra la base local · nota: ver la propuesta de Mario sobre estas tools
	nota: PR #21 aprobado e integrado en dev; herramientas y pruebas incorporadas
- [x] **S1-41** Pantallas del chat y línea de pasos con MSW · vence: 2026-11-13 · depende: S1-30, S1-35 · listo cuando: el chat muestra respuestas y pasos con eventos SSE simulados
	nota: PR #20 actualizado con tipo y fuentes; comprobaciones de GitHub aprobadas; pendiente de integración con el PR #13 de Yael y unificación de MSW

## Semana 3 · 23 al 29 nov
- [x] **S3-33** Endpoint SSE real del chat · vence: 2026-11-24 · apoyo: carlos-ramos · depende: S3-15 · listo cuando: el endpoint transmite los pasos y la respuesta de stream_chat con el formato del contrato y guarda los pasos con cada mensaje
	nota: PR #38 en borrador y con comprobaciones aprobadas; pendiente completar interrupciones, concurrencia e integración con herramientas reales
- [ ] **S3-34** Chat sin MSW en dev · vence: 2026-11-24 · depende: S3-33 · listo cuando: en dev, el chat global y el panel del caso responden con la línea de pasos y su resumen
	nota: PR #40 en borrador y con comprobaciones aprobadas; chat global y contextual probados localmente sin MSW, pendiente integración y verificación en dev
- [x] **S3-35** Agente de casos en el chat · vence: 2026-11-24 · apoyo: yael, carlos-ramos · depende: S3-15 · listo cuando: "¿por qué se rechazó la factura X?" responde con la regla y la evidencia usando consultar_caso y consultar_bitacora
	nota: implementada y validada localmente con MCP y PostgreSQL reales; pendiente revisión del PR, integración y validación en dev
- [x] **S3-36** Prueba de punta a punta del chat · vence: 2026-11-28 · depende: S3-34 · listo cuando: una prueba automatizada manda una pregunta de gobernanza y otra de casos y verifica los pasos y la respuesta
	nota: dos pruebas automatizadas de navegador aprobadas localmente con MCP y PostgreSQL reales, cubren gobernanza y casos con pasos, fuentes, evidencia y persistencia; pendiente validación del entorno compartido
