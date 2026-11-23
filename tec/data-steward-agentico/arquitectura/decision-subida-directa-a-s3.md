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


## Actualización 2026-11-23 (implementada, S3-04)
Sesión: [[tec/data-steward-agentico/sesiones/2026-11-23-juan-pablo-semana-3-y-subida-s3|semana 3 y subida a S3]].
- **Endpoint:** `POST /api/casos/url-subida` en `backend/api/subidas.py` del repo de código (PR 31). Desplegado y probado en dev.
- **Entrada:** `nombre_archivo`, `tipo_documento` (`Factura` o `Validación con políticas`) y, opcional, `tamano_bytes`.
- **Salida:** `upload_url`, `s3_key` (`casos/<uuid>/<archivo>`), `expira_en_segundos` (900) y `content_type`. El navegador sube con `PUT` y esa cabecera `Content-Type`, que va dentro de la firma: si manda otra, S3 responde 403.
- **Validación al firmar:** por extensión según el tipo de caso (facturas en PDF, PNG o JPG; validación con políticas en CSV, Excel o PDF) y nombre saneado. La validación por contenido, que pide el "Cuidado" de arriba, ocurre al procesar el archivo (la extracción abre la imagen y rechaza lo que no es válido).
- **Tamaño:** máximo de 20 MB solo como revisión de cortesía; una URL de `PUT` no puede imponerlo. Imponerlo requeriría un POST prefirmado con `content-length-range`.
- **Credenciales:** en dev y prod, el perfil de la EC2 (`LabInstanceProfile`, IMDSv2 con salto 2 para los contenedores). En local, el S3 de SeaweedFS con `S3_ENDPOINT_PUBLICO`.
- **Pendiente:** que la pantalla de subida la use (S3-31) y aceptar `.xml` para los CFDI (S3-38).
