---
tipo: agente
fecha: 2026-11-04
resumen: Agente del chat que responde dudas de gobernanza de datos: políticas, términos de negocio, dueños, clasificación de sensibilidad y calidad.
---
# Agente: Gobernanza

- **Grafo:** chat. Lo llama el [[tec/data-steward-agentico/agentes/agente-enrutador|Enrutador]].
- **Ejemplos:** "¿Quién es el dueño de los datos de proveedores?", "¿El RFC es dato sensible?", "¿Qué reglas de calidad aplican a la tabla de facturas?", "¿Qué significa factura conciliada?".
- **Tools:**
  - [[tec/data-steward-agentico/tools/buscar-politicas|buscar_politicas]] (tipo `gobernanza`)
  - [[tec/data-steward-agentico/tools/consultar-glosario|consultar_glosario]]
  - [[tec/data-steward-agentico/tools/consultar-catalogo|consultar_catalogo]]
  - [[tec/data-steward-agentico/tools/consultar-calidad|consultar_calidad]]
- **Regla clave:** cada respuesta cita su fuente (política y versión, término del glosario o ficha del catálogo); si no hay fuente, lo dice.
- **Construye:** Carlos Delgado / Carlos Ramos (las tools, Iris y Mario).
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]]


## Actualización 2026-11-04 (subequipo)
- **Subequipo:** grafo del chat, liderado por Carlos Ramos.
- **Dueño:** Mario (prompt, pruebas y evaluación). **Apoyo:** Iris y Juan Pablo.
- **Tools y sus responsables:** `consultar_glosario` (Mario), `consultar_calidad` (Iris), `consultar_catalogo` (Juan Pablo), `buscar_politicas` (Carlos Delgado / Carlos Ramos).
- Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|subequipos de agentes]].


## Actualización 2026-11-09 (Mario)
Fuentes listas para las preguntas de ejemplo de esta nota:

| Pregunta | Tool | Lo que responde |
|---|---|---|
| ¿Quién es el dueño de los datos de proveedores? | `buscar_politicas` (tipo `gobernanza`) o `consultar_catalogo` | P-021 §3: Dirección de Compras; data steward, Datos Maestros de Compras |
| ¿El RFC es dato sensible? | `buscar_politicas` (tipo `gobernanza`) | P-020 §3: sí en personas físicas (clientes), interno en personas morales (proveedores) |
| ¿Qué reglas de calidad aplican a la tabla de facturas? | `consultar_calidad` | 5 reglas; 3 no alcanzan su umbral |
| ¿Qué significa factura conciliada? | `consultar_glosario` | Definición, dueño y fuente (métrica `tasa_conciliacion`) |

- El catálogo de datos (34 fichas con data owner, data steward, sensibilidad, origen y columnas) ya está en las tablas `catalogo_tablas` y `catalogo_columnas` para `consultar_catalogo` (Juan Pablo).
- Las 4 políticas de gobernanza (P-020 a P-023) llevan `tipo: gobernanza`; las de facturas, `tipo: facturas`.
- Pendiente: prompt y conjunto de preguntas de prueba con su fuente esperada.


## Actualización 2026-11-09 (prompt y evaluación)
- **Prompt:** `datos/agentes/gobernanza.md` en el repo de código. Usa 4 tools, cita cada fuente con su identificador exacto y termina con la línea `Fuentes: …`. Si no hay fuente empieza con "No encontré"; si la pregunta es de cifras o de un caso responde "Esta pregunta no es de gobernanza.". El rol sale del JWT, no del texto.
- **Preguntas de prueba:** 35 en `datos/evaluacion/preguntas_gobernanza.yaml` (14 de políticas, 6 de glosario, 4 de catálogo, 3 de calidad, 4 sin fuente, 1 mixta, 2 fuera de dominio y 2 de seguridad), cada una con tool, fuente y lo que debe decir.
- **Evaluación:** `scripts/evaluar_gobernanza.py fuentes` revisa sin LLM que cada fuente exista y diga lo esperado (35/35). `respuestas --archivo salidas.jsonl` califica al agente: tool, cita, contenido, comportamiento y fugas de datos personales.
- **Pendiente:** conectar con Carlos Ramos y correr `respuestas` con el modelo del chat. Necesita `consultar_catalogo` (Juan Pablo).
