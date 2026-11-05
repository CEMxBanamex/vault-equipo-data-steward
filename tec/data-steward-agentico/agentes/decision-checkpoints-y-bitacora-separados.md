---
tipo: decision
fecha: 2026-10-21
resumen: Los checkpoints de LangGraph son el estado operativo del caso; la bitácora de auditoría es una tabla propia y es el registro oficial.
---
# Decisión: checkpoints y bitácora separados

- **Contexto:** LangGraph guarda el estado del grafo en checkpoints, y el proyecto también necesita un registro auditable de cada hallazgo y decisión.
- **Decisión:**
  - Checkpoints con `PostgresSaver` por `thread_id`, en el mismo RDS. Sirven para pausar en la revisión humana, recuperarse de fallos y que cualquier instancia retome un caso.
  - Bitácora en su propia tabla de PostgreSQL, escrita con la tool `registrar_hallazgo`, con exportación periódica a S3.
- **Por qué:** el checkpoint cambia con cada paso y su formato depende de LangGraph; no sirve como registro oficial. La bitácora tiene un formato propio, estable y pensado para auditoría.
- **Relacionado:** el RAG también vive en el mismo RDS, en una tabla con `pgvector` que guarda fuente, versión y vigencia de cada política.
- **Alternativas descartadas:** usar los checkpoints como bitácora.
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]]
