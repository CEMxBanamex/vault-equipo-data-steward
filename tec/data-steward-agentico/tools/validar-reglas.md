---
tipo: tool
fecha: 2026-11-04
resumen: Evalúa en código las reglas del catálogo sobre los campos extraídos y devuelve el resultado de cada regla con su versión y evidencia.
---
# Tool: validar_reglas

- **Qué hace:** aplica las reglas deterministas del catálogo, por ejemplo subtotal + impuestos = total, campos obligatorios presentes y duplicados.
- **Recibe:** campos extraídos del caso y tipo de documento.
- **Devuelve:** lista de resultados por regla: identificador, versión, cumple o no, evidencia y diferencia cuando aplica, más un resultado sugerido (aceptado, rechazado o requiere revisión).
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-validador|Validador]].
- **Implementa:** Iris / Mario.
- **Paso:** "Validando reglas…".
- **Reglas:** el LLM nunca hace estas cuentas. Con pruebas unitarias por regla. Ver [[tec/data-steward-agentico/agentes/decision-validaciones-deterministas-en-codigo|decisión]].
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]]


## Actualización 2026-11-04
- **Implementa:** Iris (antes Iris / Mario), porque ella define el catálogo de reglas. Ver [[tec/data-steward-agentico/plan-de-trabajo/decision-reparto-de-tools-y-subequipos-de-agentes|reparto de tools]].


## Actualización 2026-11-09 (implementación)
- **Estado:** lista, con pruebas unitarias por regla. Código en el repo de código: `datos/steward_datos/reglas/motor.py` y `datos/steward_datos/tools/validar_reglas.py`.
- **Recibe (`ValidarReglasEntrada`):** `caso_id`, `historia` (1 facturas, 2 registros), `factura` (salida de `extraer_campos_factura`) o `registros` (tabla de `leer_documento`), `sha256` del archivo y `fecha_recepcion`.
- **Devuelve (`ResultadoValidacion`):** `reglas_evaluadas` con versión (`R-014@2.1`), `hallazgos` (regla, versión, política, efecto, severidad, título, texto, cifras esperado/encontrado/diferencia, campos, filas y evidencia con página y caja) y `resultado_sugerido` con su `motivo`.
- **Lee de la base:** padrón de proveedores (R-017), entidades receptoras (R-018) y facturas anteriores para duplicados (R-015). No escribe; guardar es tarea de `registrar_hallazgo` o de `persistencia.guardar_resultado`.
- **Precedencia:** revisión humana > rechazo > aceptado. Ver la actualización del [[tec/data-steward-agentico/agentes/agente-validador|Validador]].
- **Catálogo:** 20 reglas en `datos/reglas/catalogo.yaml`; tabla legible en `docs/datos/catalogo_reglas.md`.


## Actualización 2026-11-09 (tarde)
- **Hallazgos con cita completa:** `HallazgoOut` agrega `politica_version` y `politica_seccion` (opcionales, del catálogo). No cambia cómo se guardan.
- **R-003 sin confianza:** si el modelo de visión no da confianza en un campo usado por las reglas, ya no se omite en silencio: se agrega un hallazgo R-003 que lista esos campos. Con `sin_confianza: informativo` (por defecto) no cambia el resultado; con `revision`, el caso va a revisión humana. Se cambia en `datos/reglas/catalogo.yaml`.
