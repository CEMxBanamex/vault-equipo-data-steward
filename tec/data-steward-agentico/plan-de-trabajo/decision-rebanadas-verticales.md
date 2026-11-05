---
tipo: decision
fecha: 2026-10-28
resumen: Cada equipo es dueño de su función de punta a punta: el frontend hace los endpoints de sus pantallas, agentes entrega funciones de Python y datos es dueño de las tools que leen y escriben la base.
---
# Decisión: reparto por rebanadas verticales

- **Contexto:** la capa de APIs (FastAPI) conecta todo, y es donde más se traban los equipos si una persona hace todo el backend y otra todo el frontend.
- **Decisión:**
  - **Frontend:** cada quien hace sus pantallas y los endpoints que esas pantallas usan (casos, decisión, bitácora, URL prefirmada, chat y SSE).
  - **Agentes:** no exponen HTTP. Entregan funciones de Python que los endpoints llaman: `procesar_caso`, `reanudar_caso` y `stream_chat`.
  - **Datos (Iris y Mario):** dueños de las tools que trabajan con la base y del endpoint de políticas para el administrador.
  - **JP:** la parte transversal: dependencia de usuario actual, permisos por rol, formato de errores y CORS.
- **Endpoints principales:** `POST /casos/url-subida`, `POST /casos`, `GET /casos`, `GET /casos/{id}`, `POST /casos/{id}/decision`, `GET /bitacora`, endpoints de conversaciones e historial del chat, mensajes del chat por SSE y `POST /politicas`.
- **Por qué:** quien hace la pantalla sabe qué datos necesita, se elimina la espera entre equipos y la frontera con agentes queda limpia. Iris y Mario quedan con un frente completo de punta a punta.
- **Apoyos:** colección de Postman compartida en el repo y MSW en el frontend mientras el backend no exista.
- **Alternativas descartadas:** una sola persona con todo el backend de APIs.
- **Enlaces:** [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]], [[tec/data-steward-agentico/plan-de-trabajo/decision-contratos-primero|contratos primero]]
