---
tipo: propuesta
fecha: 2026-11-09
autor: mario
resumen: Las vistas, el usuario de solo lectura, el registro de consultas y el catálogo ya están en la base para ejecutar_consulta, listar_vistas_consultables y consultar_catalogo; falta bloquear set_config en la validación del SQL.
---
# Propuesta: vistas y datos para la consulta libre y el catálogo

- **Notas que se cambiarían:** [[tec/data-steward-agentico/tools/ejecutar-consulta|ejecutar_consulta]], [[tec/data-steward-agentico/tools/listar-vistas-consultables|listar_vistas_consultables]] y [[tec/data-steward-agentico/tools/consultar-catalogo|consultar_catalogo]] (Juan Pablo).
- **Qué ya está en la base** (repo de código, migración `0002`):
  - **Vistas:** `v_facturas`, `v_proveedores`, `v_casos`, `v_hallazgos`, `v_ordenes_compra`, `v_pagos`, `v_centros_costo` y `v_clientes`. Las columnas, con descripción, sensibilidad y ejemplos no sensibles, están en `catalogo_columnas` (`consultable = true` en `catalogo_tablas`). Tabla legible en `docs/datos/vistas_y_catalogo.md`.
  - **Seguridad por fila:** antes de ejecutar, `steward_datos.contexto.fijar_en_bd(sesion, usuario)` hace `SET LOCAL app.rol` y `app.usuario`. Sin eso, las vistas no devuelven filas.
  - **Usuario `steward_consultas`:** si existe al migrar, recibe solo `SELECT` sobre las vistas y un `statement_timeout` de 5 s.
  - **Registro de consultas:** `consultas_libres` (pregunta, SQL, rol, usuario, si fue válida, motivo, filas y duración), para la mejora continua.
  - **Catálogo:** `catalogo_tablas` y `catalogo_columnas` con data owner, data steward, sensibilidad, origen, tablas relacionadas y término del glosario.
- **Qué propongo:**
  - En la validación con `sqlglot`, aceptar solo una lista blanca de funciones y rechazar `set_config`, `current_setting`, `pg_*`, `dblink` y similares. Una consulta como `SELECT set_config('app.rol', 'administrador', true), * FROM v_clientes` cambiaría el rol dentro de la misma transacción y se saltaría la seguridad por fila y el enmascaramiento.
  - Que `listar_vistas_consultables` lea `catalogo_tablas` y `catalogo_columnas` (solo `consultable = true`) en lugar de describir las vistas a mano.
  - Que Infraestructura cree los usuarios `steward_backend`, `steward_mcp` y `steward_consultas` antes de correr las migraciones, para que se otorguen los permisos.
- **Por qué:** así la consulta libre usa los mismos permisos que las métricas y el catálogo no se duplica.
- **Estado:** pendiente


## Actualización 2026-11-09 (verificado)
- **El riesgo es real y más amplio:** reproducido con `steward_consultas`. Incluso en un solo SELECT (`SELECT count(*) FROM (SELECT set_config('app.rol','administrador',true)) s, LATERAL (SELECT * FROM v_clientes) c`) un analista ve los 600 clientes con RFC completo. Validar "un solo SELECT" no basta.
- **Ya en el repo de código (migración `0003`):** se quita `set_config` a `PUBLIC` y se deja solo a `steward_backend`, `steward_mcp` y a quien migra. `fijar_en_bd` ahora usa `SET LOCAL` con rol y usuario validados, así que funciona con `steward_consultas`. Hay pruebas del ataque.
- **Ojo en RDS:** si el usuario maestro no es dueño de `set_config`, el `REVOKE` no hace nada sin dar error. La migración lo detecta y avisa con un `WARNING`; en ese caso hay que pedirlo a soporte o quedarse solo con la validación del SQL.
- **Sigue siendo necesario:** la lista blanca de funciones en `sqlglot` y conectarse como `steward_consultas`.
