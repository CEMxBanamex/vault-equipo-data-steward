---
tipo: agente
fecha: 2026-11-04
resumen: Punto de entrada del chat: clasifica la pregunta por dominio, la manda al agente o agentes que correspondan y combina las respuestas en las preguntas mixtas.
---
# Agente: Enrutador

- **Grafo:** chat. Primer nodo.
- **Qué hace:** clasifica cada pregunta con salida estructurada en una intención:
  - **Gobernanza** → [[tec/data-steward-agentico/agentes/agente-de-gobernanza|Agente de gobernanza]]
  - **Consultas** → [[tec/data-steward-agentico/agentes/agente-analista-de-datos|Analista de datos]]
  - **Casos** → [[tec/data-steward-agentico/agentes/agente-de-casos|Agente de casos]]
  - **Mixta:** hasta 2 dominios en secuencia y una respuesta combinada con las fuentes de ambos.
  - **General:** responde directamente, etiquetado como información general.
  - **Fuera de alcance:** respuesta fija que explica qué sí puede hacer.
- **Tools:** ninguna; solo enruta y compone.
- **Contexto que recibe:** la pregunta, el historial de la conversación, el rol del usuario y el `caso_id` si el chat está dentro de un caso.
- **Construye:** Carlos Delgado / Carlos Ramos.
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]], [[tec/data-steward-agentico/chat/decision-enrutador-por-dominio-y-capa-semantica|decisión]]


## Actualización 2026-11-04 (subequipo)
- **Subequipo:** grafo del chat, liderado por Carlos Ramos.
- **Dueño:** Carlos Ramos (enrutador e intención mixta).
- Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|subequipos de agentes]].
