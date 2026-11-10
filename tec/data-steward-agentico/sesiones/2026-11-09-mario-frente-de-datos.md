---
tipo: sesion
fecha: 2026-11-09
autor: mario
resumen: Frente de datos con Iris (4 al 9 nov.); de mi parte quedaron las vistas con seguridad por fila, los datos de negocio, el catálogo, el glosario, las métricas, las políticas de gobernanza, obtener_metrica y consultar_glosario.
---
# Sesión 2026-11-09: frente de datos (parte de Mario)

Trabajo en pareja con Iris. Su sesión del mismo día cubre `validar_reglas`, `consultar_calidad`, el catálogo de reglas y los casos de referencia. El código está en el repo de código, carpeta `datos/` (rama `datos/fases-0-a-4`), con su `README.md`.

## Qué se hizo
- **Vistas consultables** (migración `0002`): `v_facturas`, `v_proveedores`, `v_casos`, `v_hallazgos`, `v_ordenes_compra`, `v_pagos`, `v_centros_costo` y `v_clientes`.
- **Seguridad por fila sobre las vistas:** el backend fija `app.rol` y `app.usuario` con `SET LOCAL` en cada transacción. El administrador ve todo, un analista solo sus entidades (tabla `usuarios_entidades`) y sin contexto no se ve nada. En `v_clientes`, el RFC y el correo se enmascaran para quien no es administrador.
- **Usuario `steward_consultas`:** solo `SELECT` sobre las vistas, con un tiempo máximo de 5 s por consulta.
- **Datos de negocio sintéticos:** 12 meses (nov. 2025 a oct. 2026) con 960 facturas ya revisadas, 861 órdenes de compra, 8 centros de costo en 3 entidades, pagos de Tesorería y 600 clientes. Tienen errores a propósito para que haya hallazgos y reglas de calidad que fallan.
- **Contenido de gobernanza:**
  - Catálogo de datos: 34 tablas y vistas, con data owner, data steward, sensibilidad, origen y descripción y ejemplos por columna.
  - Glosario: 32 términos con dueño y fuente.
  - 12 métricas de la capa semántica.
  - Políticas de gobernanza P-020 (clasificación), P-021 (roles y dueños), P-022 (calidad) y P-023 (acceso desde el chat).
- **[[tec/data-steward-agentico/tools/obtener-metrica|obtener_metrica]] y [[tec/data-steward-agentico/tools/consultar-glosario|consultar_glosario]]:** listas, con pruebas.
- **Compatibilidad con lo ya decidido:**
  - Embeddings: `embeddinggemma:300m`, de 768 dimensiones (decisión de Carlos Delgado).
  - `buscar_politicas` filtra por `tipo` (`facturas` o `gobernanza`), como pide su nota.
  - Los IDs, montos y hallazgos de la demo coinciden con el mockup.

## Decisiones
- **Qué datos de negocio:** como el socio formador no ha dicho qué espera consultar, se cubrió el ciclo de cuentas por pagar: proveedores, órdenes de compra, facturas, pagos y centros de costo, además de los clientes de la Historia 2. Si piden otro dominio, se agrega con el mismo patrón (tabla, vista con filtro por entidad, ficha de catálogo y métricas).
- **Las facturas de negocio son casos** con `origen = negocio` (`F-0001` a `F-0960`), sin archivo. Así `buscar_facturas`, las métricas y las vistas leen una sola fuente, y los hallazgos por regla salen del mismo motor.
- **Seguridad por fila en las vistas, no en las tablas:** el usuario de consultas no tiene acceso a las tablas y el filtro vive dentro de cada vista. El backend y el MCP no se ven afectados.

## Pendientes
- Confirmar con el socio formador los datos de negocio.
- Revisar con Juan Pablo la validación del SQL libre: debe rechazar `set_config` y `current_setting`, que permitirían saltarse la seguridad por fila. Ver [[tec/data-steward-agentico/tools/propuesta-vistas-para-consulta-libre-mario|propuesta]].
- Prompt y pruebas del [[tec/data-steward-agentico/agentes/agente-de-gobernanza|agente de gobernanza]].

## Siguiente paso
Conectar `obtener_metrica` y `consultar_glosario` al grafo del chat con Carlos Ramos, y escribir las preguntas de prueba del agente de gobernanza.
