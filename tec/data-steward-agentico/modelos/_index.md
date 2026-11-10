---
tipo: area
fecha: 2026-10-21
resumen: Inferencia con Ollama en las 5 laptops con GPU del equipo: reparto por rol, embeddings, la LSTM auxiliar y el plan B con Bedrock.
---
# modelos

## Qué cubre
- Los modelos viven en el disco de cada laptop y los corre Ollama; no se despliegan en AWS. El proceso de conexión está en [[tec/_compartido/ollama-gpus-por-tailscale|Ollama en laptops del equipo vía Tailscale]].
- Reparto entre las 5 GPUs por rol: visión, razonamiento y explicación, embeddings y respaldo. En evaluaciones por lote, también por caso.
- Se fija la etiqueta exacta de cada modelo.
- La LSTM se entrena en una laptop, sus pesos se guardan en S3 y la inferencia corre dentro del MCP.
- Plan B si el modelo de visión no alcanza: Amazon Bedrock con el mismo grafo.

## Notas
- [[tec/data-steward-agentico/modelos/decision-inferencia-en-laptops|Decisión: inferencia en las laptops del equipo, no en AWS]]
- [[tec/data-steward-agentico/modelos/decision-lstm-como-auxiliar|Decisión: la LSTM es solo un modelo auxiliar]]
- [[tec/data-steward-agentico/modelos/mismo-modelo-de-embeddings|Aprendizaje: el mismo modelo de embeddings al indexar y al consultar]]

## Pendientes
- Registrar la VRAM de cada GPU y asignar modelo y rol a cada laptop.
- Probar el modelo de visión con algunas facturas de FATURA antes de comprometerse con él.


## Actualización 2026-10-28
- **Se quita la LSTM:** ya no hay modelo de anomalías ni pesos en S3. Ver [[tec/data-steward-agentico/modelos/decision-se-quita-la-lstm|Decisión: se quita la LSTM]].
- **Rol nuevo de chat:** el chat necesita un modelo (no de razonamiento, porque solo se muestran los pasos del agente). Lo puede cubrir la laptop de razonamiento y explicación o una dedicada, según la VRAM.
- **Responsables:** Carlos Delgado y Carlos Ramos. Ver [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]].

<!-- indice-automatico:inicio -->
## Índice automático
_No edites esta sección: la regenera GitHub Actions en cada cambio a main._

| Nota | Tipo | Autor | Fecha | Resumen |
|---|---|---|---|---|
| [[tec/data-steward-agentico/modelos/mismo-modelo-de-embeddings\|mismo-modelo-de-embeddings]] | aprendizaje |  | 2026-10-21 | El modelo de embeddings, con su etiqueta exacta, tiene que ser el mismo al indexar las políticas y al consultarlas; si cambia, hay que reindexar. |
| [[tec/data-steward-agentico/modelos/decision-inferencia-en-laptops\|decision-inferencia-en-laptops]] | decision |  | 2026-10-21 | El LLM, la visión y los embeddings corren con Ollama en las 5 laptops con GPU del equipo, conectadas por Tailscale, y no en AWS; el plan B es Bedrock con el mismo grafo. |
| [[tec/data-steward-agentico/modelos/decision-lstm-como-auxiliar\|decision-lstm-como-auxiliar]] | decision |  | 2026-10-21 | La LSTM que pidió el socio formador se usa solo para detectar anomalías; no interpreta instrucciones, no recupera políticas y no justifica decisiones. |
| [[tec/data-steward-agentico/modelos/decision-se-quita-la-lstm\|decision-se-quita-la-lstm]] | decision |  | 2026-10-28 | El socio formador ya no pide la LSTM; se quita la tool detectar_anomalia y en su lugar se agregan el chat y los pasos del agente visibles. |
| [[tec/data-steward-agentico/modelos/decision-modelo-embeddings-embeddinggemma\|decision-modelo-embeddings-embeddinggemma]] | decision | carlos-delgado | 2026-11-09 | Seleccionar embeddinggemma:300m para los embeddings del prototipo tras una prueba inicial de recuperación. |
| [[tec/data-steward-agentico/modelos/decision-modelo-vision-gemma3\|decision-modelo-vision-gemma3]] | decision | carlos-delgado | 2026-11-09 | Mantener gemma3:4b como candidato de visión para el prototipo y documentar sus resultados y limitaciones. |
| [[tec/data-steward-agentico/modelos/inventario-gpus-y-reparto-modelos\|inventario-gpus-y-reparto-modelos]] | decision | carlos-delgado | 2026-11-10 | Inventario de las cinco GPUs del equipo y propuesta inicial de reparto para visión, chat, embeddings y respaldo. |
| [[tec/data-steward-agentico/modelos/propuesta-confianza-y-evaluacion-vision-iris\|propuesta-confianza-y-evaluacion-vision-iris]] | propuesta | iris | 2026-11-09 | Pedir confianza por campo al modelo de visión y medirlo con las facturas sintéticas que ya tienen respuesta esperada. |
<!-- indice-automatico:fin -->
