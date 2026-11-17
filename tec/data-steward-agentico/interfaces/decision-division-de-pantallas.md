---
tipo: decision
fecha: 2026-11-17
autor: yael
resumen: Reparto de pantallas y endpoints del frontend entre Yael (Casos y Bitácora) y Mauricio (Chat, Pasos y Login).
---
# Decisión: división de pantallas y endpoints del frontend

- **Contexto:** En el frente de Frontend, Yael y Mauricio son responsables de la interfaz en React y de los endpoints de FastAPI correspondientes a sus pantallas (rebanadas verticales). Se requería formalizar la división de pantallas para avanzar en paralelo sin conflictos.
- **Decisión:**
  - **Yael:**
    - Pantallas del flujo de casos: [[tec/data-steward-agentico/interfaces/pantalla-bandeja-de-casos|bandeja de casos]], [[tec/data-steward-agentico/interfaces/pantalla-subir-caso|subir caso]], [[tec/data-steward-agentico/interfaces/pantalla-detalle-factura|detalle de factura]] y [[tec/data-steward-agentico/interfaces/pantalla-detalle-validacion|detalle de validación]].
    - Pantalla de auditoría: [[tec/data-steward-agentico/interfaces/pantalla-bitacora|bitácora]].
    - Endpoints de FastAPI correspondientes: `GET /casos`, `GET /casos/{id}`, `POST /casos`, `POST /casos/{id}/decision`, `POST /casos/url-subida` y `GET /bitacora`.
  - **Mauricio:**
    - Pantalla de acceso: [[tec/data-steward-agentico/interfaces/pantalla-inicio-de-sesion|inicio de sesión]].
    - Pantalla y componentes de conversación: pantalla Asistente (Chat global), panel contextual de preguntas en el detalle de caso, y el componente visual de la línea de pasos del agente.
    - Endpoints de FastAPI correspondientes: endpoints de conversaciones, historial del chat y streaming de eventos SSE (`/chat/stream`).
- **Por qué:** 
  - Yael es dueño de las tools `registrar_hallazgo` y `consultar_bitacora` y del `agente-redactor-de-hallazgos`, por lo que el flujo operativo de revisión de casos y auditoría encaja directamente con su trabajo de datos y backend.
  - Mauricio es dueño de las tools `consultar_caso` y `buscar_facturas` y apoya el `agente-de-casos` del chat, por lo que el flujo conversacional y streaming encaja con su especialidad.
- **Alternativas descartadas:** Dividir por capas (uno todo el frontend y otro todo el backend), descartada porque generaba cuellos de botella y dependencias bloqueantes.
- **Enlaces:** [[tec/data-steward-agentico/interfaces/_index|interfaces]], [[tec/data-steward-agentico/plan-de-trabajo/decision-rebanadas-verticales|rebanadas verticales]], [[tec/data-steward-agentico/tareas/yael|tareas de yael]], [[tec/data-steward-agentico/tareas/mauricio|tareas de mauricio]]
