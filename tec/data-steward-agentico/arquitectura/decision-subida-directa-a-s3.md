---
tipo: decision
fecha: 2026-10-21
resumen: El navegador sube el archivo del caso directo a S3 con una URL prefirmada, sin pasar por el backend.
---
# Decisión: subida directa a S3 con URL prefirmada

- **Contexto:** los casos llegan como PDFs, imágenes, hojas de cálculo o texto, y pueden pesar. Pasarlos por FastAPI ocuparía la instancia y el ALB.
- **Decisión:** el backend emite una URL prefirmada y el navegador sube el archivo directo a S3. Después, FastAPI crea el caso y la tool `leer_documento` lo trae de S3.
- **Por qué:** el backend no carga con archivos grandes y el original queda guardado desde el inicio, que es lo que necesita la trazabilidad (el analista puede consultar el documento original).
- **Cuidado:** validar el tipo por contenido, no por extensión, y limitar el tamaño. Bucket con acceso público bloqueado y cifrado.
- **Alternativas descartadas:** subida multipart a FastAPI.
- **Enlaces:** [[tec/data-steward-agentico/arquitectura/_index|arquitectura]], [[tec/data-steward-agentico/agentes/_index|agentes]]
