---
tipo: aprendizaje
fecha: 2026-10-21
resumen: El modelo de embeddings, con su etiqueta exacta, tiene que ser el mismo al indexar las políticas y al consultarlas; si cambia, hay que reindexar.
---
# Aprendizaje: el mismo modelo de embeddings al indexar y al consultar

- Los vectores de dos modelos distintos (o de dos versiones del mismo) no son comparables. Si las políticas se indexan con uno y se consultan con otro, `buscar_politicas` devuelve resultados sin sentido y sin dar error.
- Por eso se fija la **etiqueta exacta** del modelo de embeddings en Ollama, y la laptop con el rol de embeddings es la que atiende tanto la indexación como las consultas.
- Si se cambia de modelo, hay que **reindexar todas las políticas**. Conviene guardar en la tabla del RAG qué modelo generó cada vector.
- **Enlaces:** [[tec/data-steward-agentico/modelos/_index|modelos]], [[tec/data-steward-agentico/agentes/_index|agentes]]
