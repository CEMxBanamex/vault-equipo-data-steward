---
tipo: decision
fecha: 2026-10-28
resumen: El chat por caso y el global son un solo grafo de LangGraph que primero clasifica la intención de la pregunta y luego toma la ruta y la fuente que corresponde.
---
# Decisión: un solo grafo con enrutador por intención

- **Contexto:** el chat debe responder sobre un caso, sobre todas las facturas, sobre las políticas cargadas y preguntas generales, en dos lugares de la interfaz.
- **Decisión:** un solo grafo (o subgrafo) que reutiliza el servidor MCP. Un nodo enrutador clasifica la pregunta:

| Intención | Ejemplo | Fuente |
|---|---|---|
| Sobre el caso | "¿Por qué se rechazó?" | `consultar_caso` (solo si hay caso abierto) |
| Global | "¿Cuántas facturas del proveedor X tienen diferencias?" | `buscar_facturas` |
| Políticas | "¿Qué campos exige la política de proveedores?" | `buscar_politicas` |
| General | "¿Qué es la retención de ISR?" | Conocimiento del modelo, etiquetado como general |
| Fuera de alcance | "Libera el pago" | Respuesta fija que explica qué sí puede hacer |

- **Por qué:** la diferencia entre el chat del caso y el global es solo el contexto de entrada (con o sin `caso_id`). Un grafo y un componente evitan duplicar lógica.
- **Riesgo:** un modelo local puede responder con seguridad algo fiscal desactualizado. Por eso las respuestas generales se etiquetan y se distinguen visualmente.
- **Alternativas descartadas:** dos chats separados; text-to-SQL libre para el chat global (frágil con modelos locales y difícil de justificar ante un banco).
- **Enlaces:** [[tec/data-steward-agentico/chat/_index|chat]], [[tec/data-steward-agentico/agentes/_index|agentes]]


## Actualización 2026-11-04
- Ampliada por [[tec/data-steward-agentico/chat/decision-enrutador-por-dominio-y-capa-semantica|Decisión: enrutador por dominio, tools específicas y capa semántica]]. Las intenciones ahora son gobernanza, consultas, casos, mixta, general y fuera de alcance, y cada dominio tiene su propio agente.
