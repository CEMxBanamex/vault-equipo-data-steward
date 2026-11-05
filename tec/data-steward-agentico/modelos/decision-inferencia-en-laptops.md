---
tipo: decision
fecha: 2026-10-21
resumen: El LLM, la visión y los embeddings corren con Ollama en las 5 laptops con GPU del equipo, conectadas por Tailscale, y no en AWS; el plan B es Bedrock con el mismo grafo.
---
# Decisión: inferencia en las laptops del equipo, no en AWS

- **Contexto:** el reto necesita un LLM, un modelo de visión y embeddings. El equipo tiene 5 laptops con GPU y no hay presupuesto para GPUs en la nube.
- **Decisión:** los modelos viven en el disco de cada laptop y los corre Ollama. Las instancias de EC2 llegan a ellas por Tailscale. El trabajo se reparte por rol (visión, razonamiento y explicación, embeddings, respaldo) y, en lotes, por caso.
- **Por qué:** cero costo de GPU en la nube y control total de los modelos. Los datos son sintéticos, así que salir de AWS hacia las laptops no expone información real.
- **Riesgos:** si una laptop se apaga, su rol se cae (por eso hay un nodo de respaldo), y la calidad del modelo de visión todavía no está probada.
- **Alternativas descartadas por ahora:** GPUs en EC2 (costo) y Bedrock (queda como plan B).
- **Enlaces:** [[tec/data-steward-agentico/modelos/_index|modelos]], [[tec/_compartido/ollama-gpus-por-tailscale|Ollama en laptops del equipo vía Tailscale]]
