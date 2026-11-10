---
tipo: propuesta
fecha: 2026-11-09
autor: mario
resumen: Ofrecer a los Carlos la implementación de buscar_politicas y la ingesta al RAG que ya están en el repo de código, alineadas con embeddinggemma de 768 dimensiones.
---
# Propuesta: implementación de referencia de buscar_politicas

- **Nota que se cambiaría:** [[tec/data-steward-agentico/tools/buscar-politicas|buscar_politicas]] (Carlos Delgado / Carlos Ramos).
- **Qué propongo:** tomar como base, cambiar o descartar lo que ya está en el repo de código:
  - **Ingesta (frente de datos):** las políticas se fragmentan por sección, se guardan con versión, vigencia, `tipo` y el nombre del modelo de embeddings, y la nueva versión cierra la vigencia de la anterior.
  - **Políticas cargadas:** 13, de las cuales 4 son de gobernanza.
  - **`buscar_politicas`:** filtra por `tipo` (`facturas` o `gobernanza`), por vigencia en una fecha, por historia y por reglas mencionadas, y solo compara vectores del mismo modelo. Devuelve política, versión, vigencia, sección y similitud.
  - **Modelo:** usa `embeddinggemma:300m` (768 dimensiones) por defecto, como en la decisión de Carlos Delgado.
  - **Prueba de calidad:** `scripts/evaluar_rag.py` con 27 preguntas y su política esperada, 7 de ellas de gobernanza. Mide acierto@1, acierto@5 y MRR.
- **Calibración:** con vectores de prueba sin GPU da 70 % en el primer lugar y 93 % en los primeros 5. Falta correrla con `embeddinggemma` y fijar `RAG_UMBRAL_SIMILITUD`: en su prueba las similitudes correctas fueron de 0.39 a 0.56, así que el valor de 0.30 puede quedar bajo.
- **Por qué:** se construyó antes del reparto del 4 nov.; puede ahorrarles trabajo, pero la decisión es suya.
- **Estado:** pendiente


## Actualización 2026-11-09 (umbral y filtro por regla)
- **Calibración:** `scripts/evaluar_rag.py --calibrar` mide sin umbral la similitud del fragmento correcto y la de 6 preguntas sin política, y recomienda `RAG_UMBRAL_SIMILITUD` (conservador y equilibrado). Falta correrlo con `embeddinggemma:300m` en la laptop de embeddings.
- **Propuesta nueva:** no aplicar el umbral cuando la búsqueda filtra por `reglas`. Así se pide la sección exacta de una regla; con el modelo real, un umbral de 0.30 podría descartarla y el caso iría a revisión por "sin política".
- **Para el validador:** buscar por `reglas` e `historia`, no por `tipo`. Con `tipo=facturas`, R-002 recibe P-001 en lugar de P-011 y las reglas de la Historia 2 no reciben política.
- **Relación con la [[tec/data-steward-agentico/modelos/decision-modelo-embeddings-embeddinggemma|decisión de embeddings]]:** cubre dos de sus pendientes. "Consultas sin información relevante" son las 6 preguntas sin política de `preguntas_rag.yaml`, y "integrar los vectores en la base" es la ingesta del frente de datos (`politica_fragmentos`, 768 dimensiones, con el modelo guardado en cada vector).
