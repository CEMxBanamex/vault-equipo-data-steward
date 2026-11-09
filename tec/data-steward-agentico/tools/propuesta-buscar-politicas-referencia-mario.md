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
