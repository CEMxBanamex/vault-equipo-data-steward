---
tipo: pantalla
fecha: 2026-10-28
resumen: Pantalla 3, alta de un caso en dos pasos (tipo de revisión y archivos) con sus errores de carga.
---
# Pantalla 3: subir caso

## Flujo
1. **Tipo de revisión:** dos tarjetas grandes, "Revisión de factura" y "Validación con políticas", cada una con una línea de descripción.
2. **Archivos:** zona de arrastrar y soltar, botón "Elegir archivo" y campo opcional para pegar texto.
   - Tipos admitidos, visibles: `.pdf` `.jpg` `.png` `.xls` `.xlsx` `.csv` `.md` y texto.
   - Lista de archivos con nombre, tamaño, barra de progreso y botón para quitar.
3. Botón principal **Iniciar revisión**: abre el detalle en estado "Procesando".

Aviso discreto: "Estás usando datos de prueba".

## Estados de error
- Tipo no admitido: "Este tipo de archivo no está admitido. Usa PDF, imagen, Excel, CSV, Markdown o texto".
- Archivo demasiado grande (supuesto: máximo 20 MB).
- Subida fallida, con Reintentar.

## Para implementar
- Encaja con [[tec/data-steward-agentico/arquitectura/decision-subida-directa-a-s3|subida directa a S3 con URL prefirmada]]: la barra de progreso sale del upload a S3.

← [[tec/data-steward-agentico/interfaces/_index|interfaces]]
