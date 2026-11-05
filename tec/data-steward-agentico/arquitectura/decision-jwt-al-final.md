---
tipo: decision
fecha: 2026-10-28
resumen: El login con Cognito por correo se conecta temprano en el frontend, pero la validación del JWT en las APIs se activa al final con un interruptor AUTH_MODE, para probar fácil con Postman.
---
# Decisión: login con Cognito temprano, JWT en las APIs al final

- **Contexto:** validar el JWT en cada endpoint desde el inicio obliga a conseguir un token para cada prueba y puede bloquear al equipo.
- **Decisión:**
  - Todos los endpoints usan desde el principio una dependencia `get_usuario_actual()` controlada por la variable `AUTH_MODE`.
  - `AUTH_MODE=dev`: no valida; toma usuario y rol de headers simples (`X-Usuario`, `X-Rol`) o usa uno por defecto. Se prueba con una colección de Postman compartida.
  - `AUTH_MODE=cognito`: valida el JWT contra las llaves públicas de Cognito y saca usuario y rol del claim `cognito:groups`.
  - El frontend conecta el login por correo con Cognito en la Fase 2 y manda el token en cada petición, aunque el backend lo ignore hasta la Fase 4.
- **Por qué:** nadie se bloquea por la autenticación, los permisos por rol se programan desde el inicio y al activarla el cambio queda en dos lugares (la dependencia del backend y el contexto del frontend). En local se puede seguir usando `dev`.
- **Cuidados:**
  - Mientras el backend esté en `dev`, cualquiera podría mandar `X-Rol: administrador`: el ALB se restringe por IP del equipo hasta activar `cognito`, y `dev` nunca debe quedar en el despliegue final.
  - El chat lee el SSE con `fetch` para poder mandar el header `Authorization`.
  - Postman puede obtener tokens de Cognito con su soporte de OAuth 2.0.
  - Activarlo con días de margen antes de la demo.
- **Alternativas descartadas:** validar el JWT desde el inicio.
- **Enlaces:** [[tec/data-steward-agentico/arquitectura/_index|arquitectura]], [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]]
