---
tipo: decision
fecha: 2026-10-28
resumen: El "insight de pensamiento" son los pasos del agente (no el razonamiento del modelo): una línea que cambia, se expande en lista al presionarla y queda como resumen colapsado junto a la respuesta.
---
# Decisión: pasos del agente visibles, breves y con resumen

- **Contexto:** el socio formador pidió que, al mandar un prompt, se vean comentarios de "pensamiento" antes de la respuesta.
- **Decisión:**
  - Se muestran **solo los pasos del agente** (nodos y tools reales del grafo), no el razonamiento libre del modelo.
  - **Mientras trabaja:** una sola línea con el paso actual que se va reemplazando, por ejemplo "⟳ Buscando política de IVA… ›".
  - **Al presionarla:** se abre la lista de pasos del turno con su estado (completado, en curso, pendiente, error) y un detalle opcional en gris. Se actualiza en vivo.
  - **Al llegar la respuesta:** la línea queda como resumen colapsado encima de la respuesta, por ejemplo "✓ 4 pasos · 3.2 s ›", que se puede volver a abrir. Si un paso falló: "⚠ 4 pasos, 1 con error ›".
  - Cada turno tiene su propia lista. Lo ve quien tiene el chat abierto, porque forma parte de la respuesta.
- **Por qué:**
  - Los pasos salen de eventos reales del grafo: son verificables y auditables. El razonamiento que escribe un modelo no siempre refleja cómo llegó a la respuesta.
  - Sin modelos de razonamiento el chat es más rápido y pide menos VRAM.
  - El resumen persistente refuerza el principio de verificabilidad sin ocupar espacio.
- **Implementación:**
  - Cada nodo emite su paso con `get_stream_writer()`; el grafo corre con `stream_mode` `custom` y `messages`.
  - FastAPI transmite por SSE dos tipos de evento: `paso` (con `id`, `texto`, `detalle`, `estado`) y `respuesta`. El mismo `id` se reenvía al cambiar de estado.
  - El frontend lee el stream con `fetch` (no `EventSource`, que no permite mandar el JWT en headers).
  - Catálogo fijo de mensajes cortos (máx. ~5 palabras) por nodo y tool, con el dato concreto cuando aplique.
  - Los pasos y la duración (medida por el backend) se guardan en PostgreSQL con cada mensaje, en un campo JSON `pasos`, para que el resumen sobreviva a recargar.
  - Accesibilidad: la línea es un botón con `aria-expanded` y la lista usa `aria-live="polite"`.
- **Relación con la bitácora:** el resumen es la vista breve para el usuario; la bitácora sigue siendo el registro oficial con tools, entradas, resultados y versión de cada política.
- **Alternativas descartadas:** mostrar el razonamiento del modelo (`think` de Ollama); que los pasos desaparecieran por completo al responder.
- **Enlaces:** [[tec/data-steward-agentico/chat/_index|chat]], [[tec/data-steward-agentico/agentes/decision-checkpoints-y-bitacora-separados|checkpoints y bitácora separados]]
