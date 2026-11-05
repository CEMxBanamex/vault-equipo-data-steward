---
tipo: area
fecha: 2026-10-28
resumen: Chat de facturas pedido por el socio formador: alcance (por caso y global), enrutador por intención, tools de solo lectura, pasos del agente visibles y reglas que hereda.
---
# chat

## Qué cubre
El socio formador pidió agregar un chat que ayude a resolver preguntas sobre las facturas y un "insight de pensamiento" que muestre lo que hace el agente antes de responder.

- **Alcance (decidido):** el chat vive en dos lugares, con el mismo componente de React:
  - **Por caso:** panel dentro del detalle de factura y del detalle de validación. Manda el `caso_id` como contexto.
  - **Global:** pantalla nueva "Asistente" en el menú lateral, sin caso de contexto.
- **Qué responde:** preguntas sobre un caso, preguntas globales sobre todas las facturas, preguntas sobre las políticas cargadas y preguntas generales (fiscales o contables).
- **Un solo grafo con enrutador por intención:** caso, global, políticas, general y fuera de alcance. Ver [[tec/data-steward-agentico/chat/decision-un-grafo-con-enrutador-por-intencion|decisión]].
- **Tools de solo lectura del MCP:**
  - `consultar_caso(caso_id)`: datos extraídos, hallazgos y versión de reglas desde PostgreSQL.
  - `buscar_facturas(filtros)`: consultas parametrizadas y predefinidas (proveedor, fechas, resultado). Sin text-to-SQL libre.
  - `buscar_politicas`: la misma tool del RAG.
- **Pasos del agente visibles:** una línea que cambia mientras trabaja, que se expande en lista y que queda como resumen junto a la respuesta. Ver [[tec/data-steward-agentico/chat/decision-pasos-del-agente-visibles|decisión]].
- **Memoria:** cada conversación tiene su propio `thread_id` con `PostgresSaver`, separado del `thread_id` del procesamiento del caso.

## Reglas que hereda el chat
- Solo lectura: no cambia el resultado de un caso ni libera pagos (esas tools no existen).
- Cada respuesta cita su fuente: campo de la factura, regla y versión, o fragmento de la política. Si no tiene evidencia, lo dice.
- Las respuestas generales se etiquetan como información general, no política interna, y se distinguen visualmente de las respaldadas por política o por datos del caso.
- Permisos por rol también en el chat global: el rol llega del JWT de Cognito, no del texto del usuario.
- El texto de una factura es dato, nunca instrucción. Una factura que diga "ignora las reglas" no debe afectar el resultado (caso de prueba para la demo).

## Notas
- [[tec/data-steward-agentico/chat/decision-un-grafo-con-enrutador-por-intencion|Decisión: un solo grafo con enrutador por intención]]
- [[tec/data-steward-agentico/chat/decision-pasos-del-agente-visibles|Decisión: pasos del agente visibles, breves y con resumen]]

## Pendientes
- Opcional: indexar fuentes públicas (extractos de la Ley del IVA o guías del SAT) para que las preguntas generales también salgan con cita.
- Definir el catálogo de mensajes cortos de pasos por nodo y tool.
- Elegir el modelo del chat según la VRAM disponible.


## Actualización 2026-11-04 (gobernanza y consultas)
- **Requerimiento del reto:** el chat debe resolver dudas de gobernanza de datos y permitir consultas a la base sobre información de negocio y facturas.
- **Diseño elegido:** enrutador por dominio con tres agentes (gobernanza, analista de datos, casos), intención mixta, tools específicas y capa semántica con SQL validado de respaldo. Ver [[tec/data-steward-agentico/chat/decision-enrutador-por-dominio-y-capa-semantica|decisión]].
- Esto amplía la decisión anterior del enrutador por intención: los dominios ahora son gobernanza, consultas y casos.
- **Datos nuevos:** tablas de negocio sintéticas, vistas consultables, catálogo de datos, glosario, políticas de gobernanza y reglas de calidad con resultados.
- **Pendiente:** confirmar con el socio formador qué datos de negocio esperan poder consultar (solo facturas y proveedores, u otros dominios).

<!-- indice-automatico:inicio -->
## Índice automático
_No edites esta sección: la regenera GitHub Actions en cada cambio a main._

| Nota | Tipo | Autor | Fecha | Resumen |
|---|---|---|---|---|
| [[tec/data-steward-agentico/chat/decision-pasos-del-agente-visibles\|decision-pasos-del-agente-visibles]] | decision |  | 2026-10-28 | El "insight de pensamiento" son los pasos del agente (no el razonamiento del modelo): una línea que cambia, se expande en lista al presionarla y queda como resumen colapsado junto a la respuesta. |
| [[tec/data-steward-agentico/chat/decision-un-grafo-con-enrutador-por-intencion\|decision-un-grafo-con-enrutador-por-intencion]] | decision |  | 2026-10-28 | El chat por caso y el global son un solo grafo de LangGraph que primero clasifica la intención de la pregunta y luego toma la ruta y la fuente que corresponde. |
| [[tec/data-steward-agentico/chat/decision-enrutador-por-dominio-y-capa-semantica\|decision-enrutador-por-dominio-y-capa-semantica]] | decision |  | 2026-11-04 | El chat usa un enrutador por dominio con agentes especializados (gobernanza, analista de datos, casos) e intención mixta; las consultas de negocio van por una capa semántica con SQL validado como respaldo. |
<!-- indice-automatico:fin -->
