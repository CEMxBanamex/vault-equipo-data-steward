---
tipo: decision
fecha: 2026-10-21
resumen: El servidor MCP no expone ninguna tool para liberar pagos ni ejecutar operaciones, así que el límite del agente lo impone la arquitectura y no solo el prompt.
---
# Decisión: ninguna tool para liberar pagos

- **Contexto:** el principio del MVP es "el agente recomienda, la persona decide". Un prompt que diga "no apruebes pagos" se puede saltar.
- **Decisión:** el MCP solo expone tools de lectura, extracción, validación, detección y registro. No existe ninguna tool que libere pagos o ejecute operaciones.
- **Por qué:** si la acción no existe, el agente no puede hacerla aunque el prompt falle. La decisión queda en el `interrupt` del grafo, donde el analista revisa evidencia, regla y versión.
- **Consecuencia:** las etiquetas aceptado, rechazado y requiere revisión humana describen el cumplimiento de las reglas, no una aprobación operativa.
- **Alternativas descartadas:** una tool de aprobación protegida solo por instrucciones.
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]], [[tec/data-steward-agentico/producto/_index|producto]]
