---
tipo: decision
fecha: 2026-10-21
resumen: La LSTM que pidió el socio formador se usa solo para detectar anomalías; no interpreta instrucciones, no recupera políticas y no justifica decisiones.
---
# Decisión: la LSTM es solo un modelo auxiliar

- **Contexto:** el socio formador pidió incluir una LSTM. El razonamiento, la recuperación de políticas y las explicaciones ya los cubren el LLM y el RAG.
- **Decisión:** la LSTM es un modelo auxiliar de detección de anomalías, expuesto como la tool `detectar_anomalia`. Se entrena en una laptop, sus pesos se guardan en S3 y la inferencia corre dentro del contenedor del MCP.
- **Por qué:** cumple la petición sin poner un modelo secuencial a hacer algo para lo que no sirve. Su resultado es una señal más que el agente cita como evidencia.
- **Alternativas descartadas:** usar la LSTM como componente central del agente.
- **Enlaces:** [[tec/data-steward-agentico/modelos/_index|modelos]], [[tec/data-steward-agentico/agentes/_index|agentes]]


## Actualización 2026-10-28
- **Decisión reemplazada:** el socio formador ya no pide la LSTM y se quitó del proyecto. Ver [[tec/data-steward-agentico/modelos/decision-se-quita-la-lstm|Decisión: se quita la LSTM]].
