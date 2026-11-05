---
tipo: tool
fecha: 2026-11-04
resumen: Manda la factura al modelo de visión y devuelve sus campos en JSON con nivel de confianza por campo.
---
# Tool: extraer_campos_factura

- **Qué hace:** envía la imagen o el texto de la factura al modelo de visión en Ollama (por Tailscale) con salida estructurada.
- **Recibe:** el contenido preparado por `leer_documento`.
- **Devuelve:** campos de la factura (folio, proveedor, fecha, subtotal, impuestos, total, conceptos) con su confianza; los campos de baja confianza quedan marcados.
- **Usada por:** [[tec/data-steward-agentico/agentes/agente-extractor-de-documentos|Extractor de documentos]].
- **Implementa:** Carlos Delgado / Carlos Ramos.
- **Paso:** "Extrayendo campos con el modelo de visión…".
- **Reglas:** no calcula ni corrige montos, solo extrae; las comprobaciones las hace `validar_reglas`. Modelo con etiqueta fija; plan B con Bedrock si el modelo local no alcanza.
- **Enlaces:** [[tec/data-steward-agentico/tools/_index|tools]], [[tec/data-steward-agentico/modelos/_index|modelos]]
