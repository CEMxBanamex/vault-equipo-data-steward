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
- [x] **S1-27** Servidor MCP base y tool de ejemplo con la convención · vence: 2026-11-12 · apoyo: carlos-ramos · depende: S1-06 · listo cuando: el MCP corre en local con una tool de ejemplo que maneja rol, errores, pasos y pruebas, documentada para copiarla
- [x] **S1-28** Esqueleto del grafo de casos con tools falsas · vence: 2026-11-13 · depende: S1-27 · listo cuando: procesar_caso recorre extractor, validador y redactor con tools falsas y se pausa para la decisión del analista

## Semana 3 · 23 al 29 nov
- [ ] **S3-11** Grafo de casos con tools reales y gemma3:4b · vence: 2026-11-24 · apoyo: iris, yael · listo cuando: procesar_caso procesa una factura del piloto con extracción real, validar_reglas, buscar_politicas y registrar_hallazgo reales, se pausa para la decisión y reanudar_caso la cierra · nota: ruta crítica de la demo; probar primero en local y después en dev
- [x] **S3-12** Convención de agentes documentada a partir del grafo de casos (cierra S1-32) · vence: 2026-11-23 · apoyo: carlos-ramos · listo cuando: un documento en el repo de código explica cómo se arma un agente (prompt, tools, errores, pasos y pruebas) con el grafo de casos como ejemplo · nota: destraba el grafo del chat
- [ ] **S3-13** Evaluación del flujo de casos de punta a punta · vence: 2026-11-28 · apoyo: iris · depende: S3-11 · listo cuando: los casos del piloto pasan por procesar_caso y queda documentada la precisión de extracción y de clasificación contra el resultado esperado
- [ ] **S3-37** Contexto del usuario en el servidor MCP (PR 19 del repo de código) · vence: 2026-11-23 · apoyo: carlos-ramos · listo cuando: crear_servidor fija usuario_actual con el usuario del servidor, una prueba llama a obtener_metrica por MCP sin error y el PR está fusionado en dev · nota: sin esto las tools de gobernanza fallan en el chat; ver la revisión del PR 19
- [ ] **S3-38** Vía rápida para facturas en XML (CFDI 4.0) · vence: 2026-11-26 · apoyo: juan-pablo · listo cuando: extraer_campos_factura acepta un .xml de CFDI 4.0, lo lee con código (defusedxml, sin modelo) y devuelve la misma FacturaExtraida con los campos del contrato y el UUID del timbre; el endpoint de subida acepta .xml; pruebas con al menos 3 CFDI sintéticos (correcto, total que no cuadra y RFC faltante) · nota: después de la demo; en México la factura legal es el XML y el PDF es su representación impresa. Verificar el sello y el estatus en el SAT queda como trabajo futuro
