---
tipo: decision
fecha: 2026-10-28
resumen: En la Fase 0 se acuerdan los contratos (esquema, firmas de tools, endpoints y eventos SSE) como código, para que cada equipo trabaje en paralelo con datos falsos.
---
# Decisión: contratos primero, como código

- **Contexto:** frontend, backend, agentes, tools y base de datos dependen unos de otros. Si cada quien espera al anterior, el equipo trabaja en fila.
- **Decisión:** antes de construir, se acuerdan cuatro contratos. Quien consume el dato propone el formato y quien lo produce revisa si es posible entregarlo.

| Contrato | Propone | Revisa |
|---|---|---|
| Esquema de la base de datos | Iris y Mario | Agentes y JP |
| Firmas de las tools del MCP | Agentes, con Iris y Mario para las tools de datos | Todos |
| Endpoints (OpenAPI) | Frontend, a partir de sus pantallas | Agentes y JP |
| Eventos SSE del chat | Frontend con Agentes | Todos |

- **De dónde salen:** del mockup, leyendo de la pantalla hacia atrás: pantalla → endpoint → función del agente → tool → tabla.
- **Proceso:** borrador en una carpeta `contratos/` del repo (1 a 2 días) → una sesión de revisión de 1 a 2 horas → aprobación por PR a `main` → cualquier cambio posterior solo por PR revisado por los afectados.
- **Formato:** código, no documentos. Modelos de Pydantic en un paquete compartido que usan el backend y el MCP; FastAPI genera el OpenAPI y el CI genera los tipos de TypeScript del frontend. El esquema es la primera migración de Alembic.
- **Por qué:** con los contratos fijados, cada equipo construye su parte con datos falsos en la Fase 1 y en la Fase 2 solo se conecta lo real. Si alguien rompe el contrato, el build falla en el PR.
- **Alternativas descartadas:** contratos en documentos de texto (se desincronizan del código).
- **Enlaces:** [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]]
