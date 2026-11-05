---
tipo: pantalla
fecha: 2026-10-28
resumen: Pantalla 1, entrada a la app con un solo botón; el acceso lo resuelve el proveedor externo (Cognito).
---
# Pantalla 1: inicio de sesión

## Contenido
- Panel izquierdo azul con el símbolo y la frase "El agente extrae, consulta reglas y explica cada hallazgo con evidencia. Tú revisas y decides".
- Nombre del producto, descripción corta y un solo botón: **Iniciar sesión**.
- Pie: "Prototipo · todos los datos son ficticios".
- Sin registro ni "olvidé mi contraseña".

## Estados
- Normal.
- Sesión expirada: banner de advertencia "Tu sesión expiró. Inicia sesión de nuevo".

## Para implementar
- El botón redirige al login hospedado de Cognito; al volver, abre la [[tec/data-steward-agentico/interfaces/pantalla-bandeja-de-casos|bandeja de casos]].

← [[tec/data-steward-agentico/interfaces/_index|interfaces]]
