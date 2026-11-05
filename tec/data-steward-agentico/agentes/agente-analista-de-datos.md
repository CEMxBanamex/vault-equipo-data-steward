---
tipo: agente
fecha: 2026-11-04
resumen: Agente del chat que responde consultas de negocio y de facturas: capa semántica primero, luego registros puntuales y SQL validado de respaldo.
---
# Agente: Analista de datos

- **Grafo:** chat. Lo llama el [[tec/data-steward-agentico/agentes/agente-enrutador|Enrutador]].
- **Ejemplos:** "¿Cuánto le facturó el proveedor X en octubre?", "¿Qué proveedores tienen más facturas rechazadas?", "Muéstrame las facturas rechazadas por la regla de IVA".
- **Orden de decisión:**
  1. Si encaja en una métrica definida → [[tec/data-steward-agentico/tools/obtener-metrica|obtener_metrica]].
  2. Si pide registros puntuales → [[tec/data-steward-agentico/tools/buscar-facturas|buscar_facturas]].
  3. Si no encaja → [[tec/data-steward-agentico/tools/listar-vistas-consultables|listar_vistas_consultables]] + [[tec/data-steward-agentico/tools/ejecutar-consulta|ejecutar_consulta]] (SQL validado de respaldo).
- **Transparencia:** el paso muestra la métrica usada o el SQL ejecutado; si cayó al respaldo dice "Consulta libre validada".
- **Regla clave:** explica el resultado sin inventar cifras: los números salen del resultado de la tool.
- **Construye:** Carlos Delgado / Carlos Ramos (las tools, Iris y Mario).
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]], [[tec/data-steward-agentico/chat/decision-enrutador-por-dominio-y-capa-semantica|decisión]]


## Actualización 2026-11-04 (subequipo)
- **Subequipo:** grafo del chat, liderado por Carlos Ramos.
- **Dueño:** Carlos Ramos (es el agente más difícil). **Apoyo:** Juan Pablo, Mario y Mauricio.
- **Tools y sus responsables:** `obtener_metrica` (Mario), `buscar_facturas` (Mauricio), `listar_vistas_consultables` y `ejecutar_consulta` (Juan Pablo).
- Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|subequipos de agentes]].
