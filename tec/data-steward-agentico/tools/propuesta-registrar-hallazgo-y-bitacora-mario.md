---
tipo: propuesta
fecha: 2026-11-09
autor: mario
resumen: Ofrecer a Yael la implementación de registrar_hallazgo y describir la bitácora de la base para consultar_bitacora.
---
# Propuesta: registrar_hallazgo y la bitácora en la base

- **Notas que se cambiarían:** [[tec/data-steward-agentico/tools/registrar-hallazgo|registrar_hallazgo]] y [[tec/data-steward-agentico/tools/consultar-bitacora|consultar_bitacora]] (Yael).
- **Qué ya está en la base:**
  - `bitacora` solo admite inserciones: un trigger rechaza `UPDATE` y `DELETE`, aunque los intente el backend.
  - Cada evento guarda fecha, caso, actor (agente, usuario o sistema), acción, tono, detalle, regla y versión, hallazgo y `datos` (por ejemplo, valor anterior y nuevo de una corrección).
  - Acciones: `caso_creado`, `extraccion`, `politicas_consultadas`, `regla_aplicada`, `resultado_sugerido`, `correccion`, `comentario`, `confirmacion`, `escalamiento`, `error` y `politica_cargada`.
  - Los IDs se muestran como `EV-3000` en adelante.
  - La semilla deja unos 2,200 eventos, incluidos los del mockup (corrección de fecha en F-1042, escalamiento de F-1040).
- **Qué propongo:**
  - Tomar como base `registrar_hallazgo` del repo de código (`datos/steward_datos/tools/registrar_hallazgo.py`): inserta el hallazgo y su evento en la misma transacción y rechaza reglas o versiones que no existan en el catálogo.
  - Para `consultar_bitacora`, filtrar por `caso_id`, `actor_nombre`, `accion` y rango de `fecha`, que ya tienen índice.
- **Por qué:** se construyó antes del reparto; la decisión de usarla es de Yael.
- **Estado:** pendiente
