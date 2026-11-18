---
tipo: agente
fecha: 2026-11-04
resumen: Tercer agente del grafo de casos: explica cada hallazgo con su evidencia, lo registra y deja el caso en pausa para la decisión del analista.
---
# Agente: Redactor de hallazgos

- **Grafo:** procesamiento de casos. Paso 3 de 3.
- **Qué hace:** redacta una explicación clara por hallazgo (qué regla, qué versión, qué evidencia, qué diferencia), propone el resultado sugerido y registra todo en la bitácora. Después el grafo se pausa con `interrupt` hasta que el analista decide.
- **Tools:** [[tec/data-steward-agentico/tools/registrar-hallazgo|registrar_hallazgo]].
- **Modelo:** razonamiento y explicación.
- **Regla clave:** recomienda, no decide; si falta evidencia, marca el caso como "requiere revisión humana".
- **Construye:** Carlos Delgado / Carlos Ramos.
- **Enlaces:** [[tec/data-steward-agentico/agentes/_index|agentes]]


## Actualización 2026-11-04 (subequipo)
- **Subequipo:** grafo de casos, liderado por Carlos Delgado.
- **Dueño:** Yael (prompt, pruebas y evaluación). **Apoyo:** Carlos Delgado.
- **Tools y sus responsables:** `registrar_hallazgo` (Yael).
- Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|subequipos de agentes]].


## Actualización 2026-11-17 (implementación y prompt oficial)
- **Prompt oficial:** Documentado en el repo de código en `datos/agentes/redactor.md` por Yael.
- **Implementación:** Nodo en `backend/grafo_casos/redactor.py` integrado al flujo de LangGraph (`backend/grafo_casos/flujo.py`).
- **Estructura de la justificación:**
  - Cita explícita de `regla_id`, `regla_version`, `politica_id` y `politica_seccion`.
  - Ubicación de la evidencia en el documento original (ej. `página 1, campo total`).
  - Desglose cuantitativo de cifras: valor esperado, valor encontrado y diferencia.
- **Persistencia inmutable:** Invoca la tool [[tec/data-steward-agentico/tools/registrar-hallazgo|registrar_hallazgo]] para cada hallazgo y genera el evento de auditoría correspondiente.
- **Pausa de control:** Conecta directamente con el nodo `revision_analista` mediante `interrupt`, garantizando que ninguna operación se ejecute sin la aprobación explícita del analista en la interfaz web.
- **Pruebas:** Pruebas unitarias en `backend/grafo_casos/tests/test_redactor.py` con 5/5 casos pasando.
