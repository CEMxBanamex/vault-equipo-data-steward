---
tipo: sesion
fecha: 2026-11-17
autor: yael
resumen: Conexión del vault vía MCP, formalización de división de pantallas, stubs de FastAPI, tools de bitácora y MSW en frontend (100% Semana 1).
---
# Sesión 2026-11-17: avance completo Semana 1 frontend y bitácora

## Qué se hizo
- Configuración y verificación de conexión del vault mediante el servidor MCP de Obsidian (`trsdn-obsidian-mcp`).
- Formalización de la división de pantallas con Mauricio por escrito en [[tec/data-steward-agentico/interfaces/decision-division-de-pantallas|decision-division-de-pantallas]] (S1-34).
- Verificación, instalación de dependencias y compilación exitosa de la base del frontend en Vite + React con el sistema de diseño (S1-35).
- Creación de stubs y contratos en FastAPI para las pantallas asignadas (`casos.py` y `bitacora.py`) con sus pruebas unitarias en `test_api_stubs.py` (S1-36).
- Implementación de la tool `consultar_bitacora.py` con filtros indexados y registro en `mcp_registro.py`, probada con `test_tools_yael.py` (S1-37).
- Configuración de MSW (Mock Service Worker) en el frontend interceptando los 6 endpoints de casos y bitácora para desarrollo desacoplado (S1-38).

## Decisiones
- Se formalizó que Yael es responsable de las pantallas del flujo de casos y bitácora junto con sus endpoints, mientras que Mauricio toma login, chat y streaming SSE.
- La tool `consultar_bitacora` utiliza los índices existentes en `bitacora` (`caso_id`, `actor_nombre`, `accion`, `fecha`) garantizando lecturas inmutables.

## Pendientes
- Esperar la revisión de contratos con Juan Pablo (S1-06) y la conexión de la base de datos real en AWS/local.
- Integrar el componente visual de Pasos del Agente cuando Mauricio tenga el esqueleto del chat.

## Siguiente paso
- Arrancar la Fase 2: sustituir los datos simulados por llamadas a las funciones del grafo de LangGraph conforme Carlos Delgado y Carlos Ramos tengan los grafos conectados.
