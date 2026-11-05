---
tipo: area
fecha: 2026-10-21
resumen: Infraestructura del MVP en AWS (ALB, ASG, EC2 con Docker Compose, RDS con pgvector, S3, Cognito), qué está decidido y qué propuesto, contenedores, red y seguridad.
---
# arquitectura

## Qué cubre
- **Vista general:** navegador → ALB (HTTPS) ↔ Cognito (login y JWT) → ASG con instancias EC2 idénticas → RDS PostgreSQL + pgvector, S3 y, por Tailscale, las laptops con Ollama. Servicios de apoyo: Secrets Manager e IAM. El diagrama vive en Lucid (enlace en el README del repo) y su imagen en `resources/images/arquitectura.webp`.
- **Decidido:** AWS, ALB con ASG, Cognito, EC2 con cliente y servidor MCP en la misma instancia, FastAPI + LangGraph, Vite + React, RDS PostgreSQL con pgvector, Tailscale, Ollama en las laptops, S3 e IAM (roles por definir).
- **Propuesto:** Nginx (sirve el build y redirige `/api` al backend), Docker Compose con tres contenedores, ASG en 2 zonas con mínimo 1 y máximo 3, y Secrets Manager.
- **Contenedores de cada instancia:**
  - `frontend`: Nginx con el build de Vite + React. Puerto 80, hacia el ALB.
  - `backend`: FastAPI + LangGraph (cliente MCP). Solo red interna.
  - `mcp`: servidor MCP con las tools. Solo red interna, accesible desde el backend.
  - Tailscale se instala en la instancia. Ollama, PostgreSQL y S3 no son contenedores del despliegue.
- **Seguridad:**
  - EC2 y RDS en subredes privadas; el ALB en subredes públicas.
  - Security groups: el ALB acepta HTTPS de internet, el EC2 solo del ALB y RDS solo del EC2.
  - S3 fuera de la VPC; se recomienda un VPC Gateway Endpoint, con acceso público bloqueado y cifrado.
  - Credenciales en Secrets Manager; la instancia usa un rol de IAM, sin llaves de acceso.
  - Dos usuarios de base de datos: uno para el backend y otro, con permisos mínimos, para el MCP.

## Notas
- [[tec/data-steward-agentico/arquitectura/decision-monolito-modular|Decisión: monolito modular]]
- [[tec/data-steward-agentico/arquitectura/decision-subida-directa-a-s3|Decisión: subida directa a S3 con URL prefirmada]]
- [[tec/data-steward-agentico/arquitectura/auto-scaling-no-acelera-el-modelo|Aprendizaje: el Auto Scaling no acelera el modelo]]
- [[tec/data-steward-agentico/arquitectura/ollama-solo-por-tailscale|Aprendizaje: Ollama no tiene autenticación, solo por Tailscale]]

## Pendientes
- Confirmar Nginx, Docker Compose, la configuración del ASG y Secrets Manager.
- Definir los roles de IAM y los grupos de Cognito.
- Agregar al diagrama el título visible del ASG, el VPC endpoint de S3 y los security groups.
- Verificar los límites del plan gratuito de Tailscale.


## Actualización 2026-10-28
- Nota nueva: [[tec/data-steward-agentico/arquitectura/decision-jwt-al-final|Decisión: login con Cognito temprano, JWT en las APIs al final]] (interruptor `AUTH_MODE`, ALB restringido por IP mientras tanto).
- **Entorno local:** `docker-compose.dev.yml` con PostgreSQL + pgvector para que todos desarrollen sin depender de AWS.
- **Nginx:** cuidar el buffering para que funcione el SSE del chat detrás del ALB.
- **CI/CD (GitHub Actions):** lint y pruebas en cada PR, generación de tipos de TypeScript desde el OpenAPI, imágenes en ECR y despliegue con instance refresh del ASG al hacer merge a `main`.
- **Primer despliegue real:** al terminar la Fase 2, no al final. Ver [[tec/data-steward-agentico/plan-de-trabajo/_index|plan de trabajo]].
- Responsable de infraestructura y CI/CD: Juan Pablo.

<!-- indice-automatico:inicio -->
## Índice automático
_No edites esta sección: la regenera GitHub Actions en cada cambio a main._

| Nota | Tipo | Autor | Fecha | Resumen |
|---|---|---|---|---|
| [[tec/data-steward-agentico/arquitectura/auto-scaling-no-acelera-el-modelo\|auto-scaling-no-acelera-el-modelo]] | aprendizaje |  | 2026-10-21 | El cuello de botella son las GPUs de las laptops, así que el Auto Scaling Group no acelera la inferencia; sirve para demostrar resiliencia. |
| [[tec/data-steward-agentico/arquitectura/ollama-solo-por-tailscale\|ollama-solo-por-tailscale]] | aprendizaje |  | 2026-10-21 | Ollama no tiene autenticación, así que nunca se expone a internet; solo es alcanzable por Tailscale y con ACL limitadas al puerto 11434. |
| [[tec/data-steward-agentico/arquitectura/decision-monolito-modular\|decision-monolito-modular]] | decision |  | 2026-10-21 | Un solo repositorio y un solo servicio desplegable, con los agentes como nodos de un grafo LangGraph, porque es lo más simple de desplegar y depurar para un MVP con equipo chico. |
| [[tec/data-steward-agentico/arquitectura/decision-subida-directa-a-s3\|decision-subida-directa-a-s3]] | decision |  | 2026-10-21 | El navegador sube el archivo del caso directo a S3 con una URL prefirmada, sin pasar por el backend. |
| [[tec/data-steward-agentico/arquitectura/decision-jwt-al-final\|decision-jwt-al-final]] | decision |  | 2026-10-28 | El login con Cognito por correo se conecta temprano en el frontend, pero la validación del JWT en las APIs se activa al final con un interruptor AUTH_MODE, para probar fácil con Postman. |
<!-- indice-automatico:fin -->
