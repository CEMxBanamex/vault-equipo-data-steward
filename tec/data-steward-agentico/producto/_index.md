---
tipo: area
fecha: 2026-10-21
resumen: Qué resuelve el MVP para los analistas: principios, las dos historias de usuario, cómo se clasifica cada caso, los datos del piloto y cómo se mide el éxito.
---
# producto

## Qué cubre
- **Problema:** los analistas revisan a mano facturas, registros y documentos contra reglas y políticas internas. Es lento, con mucha captura manual, deja pasar errores y cada decisión debe poder auditarse.
- **Principios del MVP:**
  - El agente recomienda, la persona decide.
  - Cada recomendación es verificable: evidencia, regla aplicada y su versión, y acceso al original.
  - Todo queda en la bitácora de auditoría.
  - El agente no libera pagos ni ejecuta operaciones.
  - Si falta evidencia o hay incertidumbre, lo señala y pide revisión humana.
- **Historia 1, revisión de facturas (analista de cuentas por pagar):** carga una factura y obtiene sus datos estructurados, la revisión de las reglas aplicables y la explicación de las inconsistencias. Ejemplo: el total no coincide con subtotal más impuestos y el agente muestra la diferencia.
- **Historia 2, validación con políticas internas (analista de datos):** valida documentos o registros contra políticas autorizadas. Ejemplo: falta un campo obligatorio y el agente dice cuál falta y qué regla lo exige.
- **Clasificación de cada caso:** aceptado, rechazado o requiere revisión humana. Describe el cumplimiento de las reglas evaluadas; **no es una aprobación operativa**.
- **Datos del piloto:** dataset FATURA (10,000 facturas sintéticas, 50 diseños, anotaciones estructuradas). No es CFDI mexicano real, así que las reglas del piloto se definen de forma explícita. Solo datos sintéticos o autorizados.
- **Cómo se mide el éxito:** primero una línea base, comparando los mismos casos con y sin agente: tiempo de revisión, errores identificados y utilidad de las recomendaciones según los analistas. Las metas se fijan después.
- **Condiciones para un MVP confiable:** permisos por rol, datos de prueba autorizados, reglas vigentes y la posibilidad de reconstruir la justificación desde el original.

## Notas
Sin notas propias todavía; las decisiones de diseño viven en [[tec/data-steward-agentico/agentes/_index|agentes]] y [[tec/data-steward-agentico/modelos/_index|modelos]].

## Pendientes
- Acordar con el socio formador los documentos y políticas de la Historia 2 y las reglas concretas de la Historia 1.
- Medir la línea base y definir las metas de evaluación.

## Actualización 2026-10-28
- Nota nueva: [[tec/data-steward-agentico/producto/mockup-interfaz|Mockup navegable de la interfaz]] (pantallas, estados alternos y cómo reflejan los principios).
- Sesión: [[tec/data-steward-agentico/sesiones/2026-10-28-mockup-interfaz|2026-10-28 mockup de la interfaz]].
- Pendiente nuevo: recoger la retroalimentación del socio formador sobre el mockup.
- Nota nueva (2026-10-28): [[tec/data-steward-agentico/producto/deploy-mockup-vercel|Aprendizaje: deploy del mockup en Vercel]]. Mockup publicado en https://banamex-cem.vercel.app/.


## Actualización 2026-10-28 (cambio de alcance)
- El socio formador ya no pide la LSTM. Ver [[tec/data-steward-agentico/modelos/decision-se-quita-la-lstm|Decisión: se quita la LSTM]].
- Pidió un **chat** que responda preguntas sobre las facturas (por caso y global), sobre las políticas cargadas y preguntas generales, y un **insight de pensamiento**: los pasos del agente visibles mientras responde. Ver [[tec/data-steward-agentico/chat/_index|chat]].
- El chat respeta los principios del MVP: solo lectura, respuestas con fuente y respuestas generales etiquetadas como tales.
- **Para la evaluación y la demo:** la factura con instrucciones inyectadas es un caso de prueba que muestra que el texto del documento no controla al agente.


## Actualización 2026-11-04 (requerimiento de gobernanza)
- Entre los requerimientos del reto, el chat conectado al modelo debe resolver **dudas de gobernanza de datos** y permitir **consultas a la base** sobre información de negocio y de las facturas. Ver [[tec/data-steward-agentico/chat/decision-enrutador-por-dominio-y-capa-semantica|decisión]].
- **Pendiente con el socio formador:** qué datos de negocio esperan consultar.

<!-- indice-automatico:inicio -->
## Índice automático
_No edites esta sección: la regenera GitHub Actions en cada cambio a main._

| Nota | Tipo | Autor | Fecha | Resumen |
|---|---|---|---|---|
| [[tec/data-steward-agentico/producto/deploy-mockup-vercel\|deploy-mockup-vercel]] | aprendizaje |  | 2026-10-28 | El mockup está desplegado en Vercel desde la carpeta frontend del monorepo; el repo vive en la organización de GitHub, así que Vercel necesita acceso a ella. |
| [[tec/data-steward-agentico/producto/mockup-interfaz\|mockup-interfaz]] | aprendizaje |  | 2026-10-28 | Qué muestra cada pantalla del mockup navegable (Vite + React, sin conexiones), qué se puede hacer en ella y qué principio del producto refleja. |
<!-- indice-automatico:fin -->
