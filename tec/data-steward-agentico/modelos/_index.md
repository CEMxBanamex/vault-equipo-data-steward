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
