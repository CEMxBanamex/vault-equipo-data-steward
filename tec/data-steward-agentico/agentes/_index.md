---
tipo: area
fecha: 2026-10-21
resumen: El grafo de LangGraph y las tools del servidor MCP: flujo de un caso, tipos de archivo, checkpoints, RAG con pgvector y bitácora de auditoría.
---
# agentes

## Qué cubre
- **Flujo de un caso:**
  1. El analista inicia sesión (Cognito entrega el JWT) y sube el archivo directo a S3 con una URL prefirmada.
  2. FastAPI valida el JWT, crea el caso con un `thread_id` y lanza el grafo en segundo plano.
  3. Un nodo enrutador decide la ruta según el tipo de archivo.
  4. Los nodos llaman a las tools del MCP: extraer datos, consultar políticas, validar reglas y, si aplica, detectar anomalías.
  5. El grafo se pausa con `interrupt` para que el analista revise evidencia, regla y versión, y decida.
  6. Cada paso se guarda en checkpoints y la bitácora queda en PostgreSQL.
- **Tools del MCP:** `leer_documento` (trae el archivo de S3), `leer_pdf_o_excel`, `extraer_campos_factura` (modelo de visión → datos estructurados), `buscar_politicas` (pgvector, con versión), `validar_reglas` (comprobaciones exactas en código), `detectar_anomalia` (LSTM) y `registrar_hallazgo` (bitácora).
- **Tipos de archivo:**
  - `.jpg`, `.png`: visión en Ollama → JSON estructurado.
  - `.pdf`: con texto, extracción directa; escaneado, páginas a imagen → visión.
  - `.xls`, `.xlsx`, `.csv`: pandas/openpyxl → filas → validadores deterministas.
  - `.md` y texto: si es un caso, al agente; si es una política, fragmentos → embeddings → índice.
  - Dos entradas separadas: casos (analista) y políticas para el RAG (rol administrador). Validar el tipo por contenido y limitar el tamaño.
- **Memoria y RAG:**
  - Checkpoints con `PostgresSaver` por `thread_id`: pausa para revisión humana, recuperación de fallos y cualquier instancia retoma un caso.
  - RAG en una tabla con `pgvector` en el mismo RDS, con fuente, versión y vigencia de cada política. Los PDFs originales en S3.
  - Bitácora de auditoría en su propia tabla, con exportación periódica a S3.

## Notas
- [[tec/data-steward-agentico/agentes/decision-validaciones-deterministas-en-codigo|Decisión: las validaciones exactas las hace el código, no el LLM]]
- [[tec/data-steward-agentico/agentes/decision-sin-tool-para-liberar-pagos|Decisión: ninguna tool para liberar pagos]]
- [[tec/data-steward-agentico/agentes/decision-checkpoints-y-bitacora-separados|Decisión: checkpoints y bitácora separados]]

## Pendientes
- Definir las reglas concretas que implementará `validar_reglas` (dependen de lo que se acuerde con el socio formador).

## Fragmentos candidatos (no creados)
- `validar_reglas`, en particular la comprobación subtotal + impuestos = total: es el núcleo determinista de la Historia 1.
- El nodo enrutador por tipo de archivo: decide la ruta del grafo.
- La configuración de `PostgresSaver` + `interrupt`: hace posible la revisión humana y que otra instancia retome un caso.


## Actualización 2026-10-28
- **Tool eliminada:** `detectar_anomalia` (se quitó la LSTM). Ver [[tec/data-steward-agentico/modelos/decision-se-quita-la-lstm|Decisión: se quita la LSTM]].
- **Tools nuevas para el chat:** `consultar_caso` y `buscar_facturas`, de solo lectura. Las tools de datos (`validar_reglas`, `buscar_politicas`, `registrar_hallazgo`, `consultar_caso`, `buscar_facturas`) las implementan Iris y Mario; el grafo, el servidor MCP base y las tools de documentos, los dos Carlos.
- **Frontera con el backend:** el grafo se expone como funciones de Python (`procesar_caso`, `reanudar_caso`, `stream_chat`), no como endpoints. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-rebanadas-verticales|rebanadas verticales]].
- **Grafo del chat y pasos visibles:** ver el área [[tec/data-steward-agentico/chat/_index|chat]].
- **Recuperación de casos huérfanos:** detectar casos "en proceso" sin actividad y reanudarlos desde su checkpoint (Fase 4).


## Actualización 2026-11-04 (agentes y tools definitivos)
- **Grafo de procesamiento de casos (pipeline de orden fijo):**
  - Extractor de documentos: `leer_documento` (absorbe `leer_pdf_o_excel`), `extraer_campos_factura`.
  - Validador: `validar_reglas`, `buscar_politicas`.
  - Redactor de hallazgos: `registrar_hallazgo`.
- **Grafo del chat (enrutador por dominio):**
  - Agente de gobernanza: `buscar_politicas`, `consultar_glosario`, `consultar_catalogo`, `consultar_calidad`.
  - Agente analista de datos: `obtener_metrica`, `buscar_facturas`, `listar_vistas_consultables`, `ejecutar_consulta`.
  - Agente de casos: `consultar_caso`, `consultar_bitacora`.
- **Tools nuevas:** `consultar_glosario`, `consultar_catalogo`, `consultar_calidad`, `obtener_metrica`, `listar_vistas_consultables`, `ejecutar_consulta`, `consultar_bitacora`. Las implementan Iris y Mario; el usuario de solo lectura para consultas lo configura Juan Pablo.
- Ver [[tec/data-steward-agentico/chat/decision-enrutador-por-dominio-y-capa-semantica|decisión]].


## Actualización 2026-11-04 (una nota por agente)
**Grafo de procesamiento de casos**
- [[tec/data-steward-agentico/agentes/agente-extractor-de-documentos|Extractor de documentos]]
- [[tec/data-steward-agentico/agentes/agente-validador|Validador]]
- [[tec/data-steward-agentico/agentes/agente-redactor-de-hallazgos|Redactor de hallazgos]]

**Grafo del chat**
- [[tec/data-steward-agentico/agentes/agente-enrutador|Enrutador]]
- [[tec/data-steward-agentico/agentes/agente-de-gobernanza|Gobernanza]]
- [[tec/data-steward-agentico/agentes/agente-analista-de-datos|Analista de datos]]
- [[tec/data-steward-agentico/agentes/agente-de-casos|Casos]]

Las tools tienen su propia área: [[tec/data-steward-agentico/tools/_index|tools]]. Son 14 (la sección anterior de este índice decía 13 por un error de conteo).
- Corrección 2026-11-04: ninguna sección anterior de este índice decía 13 tools; el error de conteo fue solo en la conversación. Son 14.


## Actualización 2026-11-04 (subequipos)
Las secciones anteriores dicen que todos los agentes los construyen los Carlos; ahora se construyen en dos subequipos. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|decisión]].

| Grafo | Líder | Agente | Dueño | Apoyo |
|---|---|---|---|---|
| Casos | Carlos Delgado | [[tec/data-steward-agentico/agentes/agente-extractor-de-documentos\|Extractor de documentos]] | Carlos Delgado | Carlos Ramos |
| Casos | Carlos Delgado | [[tec/data-steward-agentico/agentes/agente-validador\|Validador]] | Iris | Carlos Delgado |
| Casos | Carlos Delgado | [[tec/data-steward-agentico/agentes/agente-redactor-de-hallazgos\|Redactor de hallazgos]] | Yael | Carlos Delgado |
| Chat | Carlos Ramos | [[tec/data-steward-agentico/agentes/agente-enrutador\|Enrutador]] | Carlos Ramos | — |
| Chat | Carlos Ramos | [[tec/data-steward-agentico/agentes/agente-de-gobernanza\|Gobernanza]] | Mario | Iris, Juan Pablo |
| Chat | Carlos Ramos | [[tec/data-steward-agentico/agentes/agente-analista-de-datos\|Analista de datos]] | Carlos Ramos | Juan Pablo, Mario, Mauricio |
| Chat | Carlos Ramos | [[tec/data-steward-agentico/agentes/agente-de-casos\|Casos]] | Mauricio | Yael |

- **El dueño** lleva el prompt, las pruebas y la evaluación de su agente; **el líder** se encarga del grafo completo y de que los agentes encajen.
- **Orden:** el esqueleto de los grafos arranca con tools falsas y cambia a las reales conforme salen.
- **Convención:** los Carlos dejan un agente de ejemplo (prompt, conexión de tools, pasos y pruebas) que el resto copia.
