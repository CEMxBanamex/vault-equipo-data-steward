---
tipo: tareas
fecha: 2026-11-09
autor: juan-pablo
resumen: Tareas de Juan Pablo (Infraestructura y CI/CD) por semana y su estado. Solo Juan Pablo las marca; juan-pablo agrega las de cada semana.
---
# Tareas de Juan Pablo

Frente: Infraestructura y CI/CD. Estados: `[ ]` pendiente, `[/]` en proceso, `[x]` listo, `[!]` bloqueado (agrega `· bloqueo: <motivo>`). Cambia solo la casilla y, si hace falta, `bloqueo` o `nota`. Formato y reglas: [[tec/data-steward-agentico/tareas/_index|tareas]]. Estado del equipo: [[tec/data-steward-agentico/tareas/_tablero|tablero]].

## Semana 1 · 9 al 13 nov
- [x] **S1-01** Estructura del repo de código en main · vence: 2026-11-10 · listo cuando: main del repo de código tiene backend/, mcp/, frontend/ y contratos/ junto a datos/, con un README de la estructura · nota: hecha en dev (PR 3 a 6) y llega a main con el primer PR de dev a main. contracts/ lo crea quien publique el OpenAPI
- [x] **S1-02** docker-compose.dev.yml con PostgreSQL + pgvector para todo el equipo · vence: 2026-11-10 · depende: S1-01 · listo cuando: docker compose up levanta la base y corre las migraciones de datos/ en limpio · nota: hecho en dev (PR 7), con make up, make migrate y make datos
- [x] **S1-03** CI mínimo del repo de código · vence: 2026-11-10 · depende: S1-01 · listo cuando: lint y pruebas corren en cada PR, incluidas las pruebas de datos/ · nota: ci.yml en dev (PR 8), con ci-ok como check obligatorio
- [x] **S1-04** CODEOWNERS del repo de código · vence: 2026-11-10 · depende: S1-01 · listo cuando: cada carpeta tiene dueño y el archivo está en main · nota: en dev (PR 8) y llega a main con el primer PR de dev a main. Solo sugiere revisores, no es obligatorio
- [x] **S1-05** Infra en AWS: RDS PostgreSQL con pgvector y EC2 · vence: 2026-11-10 · listo cuando: la EC2 se conecta a la base y las migraciones corren ahí · nota: bootstrap, shared y dev aplicados el 20 y 22 nov.; el primer despliegue corrió las migraciones en dsa_dev (0003) y api-dev.cem-steward.online responde. Arreglos del lab en el PR 23 del repo de código; prod se aplica al promover
- [ ] **S1-06** Sesión de revisión de contratos y PR aprobado a main #hito · vence: 2026-11-11 · apoyo: todos · depende: S1-30, S1-36, S1-39 · listo cuando: esquema, firmas de las tools, OpenAPI y eventos SSE aprobados en main · nota: usar docs/datos/sesion_contratos.md de Mario
- [x] **S1-07** Confirmar con el socio formador los datos de negocio · vence: 2026-11-11 · apoyo: mario · listo cuando: respuesta del socio formador por escrito y el supuesto de cuentas por pagar confirmado o ajustado · nota: sin contacto con el socio formador; los supuestos quedan como definitivos y las políticas de facturas se basan en el SAT (ver plan-de-trabajo/decision-supuestos-sin-socio-formador)
- [ ] **S1-08** Primera versión de ejecutar_consulta, listar_vistas_consultables y consultar_catalogo · vence: 2026-11-13 · apoyo: mario · depende: S1-06, S1-27 · listo cuando: las tres tools pasan sus pruebas contra las vistas y ejecutar_consulta rechaza set_config y current_setting · nota: ver la propuesta de Mario sobre vistas para consulta libre
- [ ] **S1-09** Login con Cognito por correo (AUTH_MODE sin validar el JWT) · vence: 2026-11-13 · apoyo: mauricio · depende: S1-35 · listo cuando: un usuario entra con su correo y el frontend recibe el JWT y su rol
- [x] **S1-10** Pipeline de imágenes a ECR · vence: 2026-11-13 · depende: S1-01 · listo cuando: un merge a main publica las imágenes de frontend, backend y mcp en ECR · nota: hecho con GHCR en vez de ECR (decisión de ramas y CI/CD); cada push a dev publica backend y mcp en GHCR y el frontend en Vercel (PR 16, 26 y 27). La promoción a main está en deploy-prod.yml y se prueba al fusionar dev a main
- [ ] **S1-11** Checkpoint del viernes (30 min) #hito · vence: 2026-11-13 · apoyo: todos · listo cuando: cada quien mostró lo suyo corriendo y el tablero refleja el estado real
