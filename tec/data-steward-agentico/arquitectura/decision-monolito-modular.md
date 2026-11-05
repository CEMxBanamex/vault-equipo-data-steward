---
tipo: decision
fecha: 2026-10-21
resumen: Un solo repositorio y un solo servicio desplegable, con los agentes como nodos de un grafo LangGraph, porque es lo más simple de desplegar y depurar para un MVP con equipo chico.
---
# Decisión: monolito modular

- **Contexto:** es un MVP de un reto, con un equipo chico y poco tiempo. El sistema tiene frontend, API, orquestación multiagente y tools.
- **Decisión:** un solo repositorio (monorepo) y un solo servicio desplegable por instancia, empaquetado con Docker Compose en tres contenedores (`frontend`, `backend`, `mcp`). Los agentes son nodos de un grafo LangGraph, no servicios separados.
- **Por qué:** se despliega y se depura en un solo lugar, y cada réplica del ASG es idéntica. Los checkpoints en PostgreSQL permiten que cualquier instancia retome un caso, así que no hace falta estado local.
- **Alternativas descartadas:** microservicios por agente (más infraestructura y más puntos de falla para un MVP).
- **Evolución posible, sin cambiar el agente:** separar el servidor MCP en su propia instancia, o mover el procesamiento de documentos a un worker con cola (por ejemplo, SQS).
- **Enlaces:** [[tec/data-steward-agentico/arquitectura/_index|arquitectura]], [[tec/data-steward-agentico/arquitectura/auto-scaling-no-acelera-el-modelo|el Auto Scaling no acelera el modelo]]
