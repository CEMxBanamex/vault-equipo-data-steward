---
tipo: decision
fecha: 2026-11-04
resumen: El chat usa un enrutador por dominio con agentes especializados (gobernanza, analista de datos, casos) e intención mixta; las consultas de negocio van por una capa semántica con SQL validado como respaldo.
---
# Decisión: enrutador por dominio, tools específicas y capa semántica

- **Contexto:** entre los requerimientos del reto, el chat conectado al modelo debe resolver dudas de **gobernanza de datos** y permitir **consultas a la base** sobre información de negocio y facturas. Se evaluaron cuatro diseños de agentes (agente único, enrutador + dominios, supervisor, planificador + verificador) y tres de tools (específicas, genéricas, capa semántica).
- **Decisión de agentes (opción B):**
  - Un **enrutador** clasifica la pregunta con salida estructurada: gobernanza, consultas, casos, mixta, general o fuera de alcance.
  - **Agente de gobernanza:** `buscar_politicas` (filtro por tipo), `consultar_glosario`, `consultar_catalogo`, `consultar_calidad`.
  - **Agente analista de datos:** `obtener_metrica`, `buscar_facturas`, `listar_vistas_consultables`, `ejecutar_consulta`.
  - **Agente de casos:** `consultar_caso`, `consultar_bitacora`.
  - **Intención mixta:** llama hasta 2 dominios en secuencia y combina las respuestas con sus fuentes.
  - Las preguntas generales se responden etiquetadas; las fuera de alcance reciben una respuesta fija.
- **Decisión de tools (opciones 1 y 3):** tools específicas por dominio y una capa semántica para las consultas de negocio. Orden del analista de datos:
  1. Si encaja en una métrica definida → `obtener_metrica` (el código genera el SQL).
  2. Si pide registros puntuales → `buscar_facturas`.
  3. Si no encaja → `listar_vistas_consultables` + `ejecutar_consulta` (SQL validado de respaldo).
- **Seguridad del SQL de respaldo:** solo vistas, usuario de base de datos de solo lectura con tiempo máximo, validación con `sqlglot` (un SELECT, vistas permitidas, límite de filas) y seguridad a nivel de fila por rol.
- **Transparencia:** el paso muestra la métrica usada o el SQL ejecutado como detalle; si cayó al respaldo dice "Consulta libre validada".
- **Mejora continua:** se registran las preguntas que caen al SQL de respaldo; las que se repiten se vuelven métricas nuevas.
- **Por qué:**
  - Con modelos locales, un clasificador con pocas opciones y agentes con 2 a 4 tools cada uno es lo más confiable para el tool calling.
  - Cada dominio se construye y evalúa por separado.
  - La capa semántica evita que el modelo escriba SQL en la mayoría de los casos, y las definiciones de métricas son en sí mismas gobernanza de datos.
- **Evolución posible:** agregar un nodo verificador al final (revisa fuentes, cifras contra el resultado del SQL y permisos del rol) sin rehacer el grafo.
- **Alternativas descartadas:** agente único con todas las tools (poco confiable con modelos locales); supervisor LLM (más lento y propenso a ciclos con modelos pequeños); planificador + verificador completo (demasiado lento en laptops); tools genéricas (pasos menos informativos).
- **Enlaces:** [[tec/data-steward-agentico/chat/_index|chat]], [[tec/data-steward-agentico/chat/decision-un-grafo-con-enrutador-por-intencion|decisión anterior del enrutador]], [[tec/data-steward-agentico/agentes/_index|agentes]]
