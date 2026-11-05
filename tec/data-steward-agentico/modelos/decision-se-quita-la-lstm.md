---
tipo: decision
fecha: 2026-10-28
resumen: El socio formador ya no pide la LSTM; se quita la tool detectar_anomalia y en su lugar se agregan el chat y los pasos del agente visibles.
---
# Decisión: se quita la LSTM

- **Contexto:** la LSTM se había incluido como modelo auxiliar de anomalías porque el socio formador la pidió ([[tec/data-steward-agentico/modelos/decision-lstm-como-auxiliar|decisión anterior]]). Ahora ya no es parte del reto; en su lugar pidió un chat de facturas y un "insight de pensamiento".
- **Decisión:** se eliminan la tool `detectar_anomalia`, el entrenamiento y los pesos en S3. El grafo de casos queda: extraer → buscar políticas → validar → explicar → revisión humana.
- **Opcional:** si se quiere conservar algo de detección de anomalías sin un modelo, se pueden agregar reglas deterministas a `validar_reglas` (facturas duplicadas, montos fuera del rango histórico del proveedor).
- **Por qué:** era la pieza más forzada del diseño y quitarla elimina MLOps que no aportaba al objetivo.
- **Enlaces:** [[tec/data-steward-agentico/modelos/_index|modelos]], [[tec/data-steward-agentico/chat/_index|chat]]
