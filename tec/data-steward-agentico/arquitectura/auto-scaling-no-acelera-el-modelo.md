---
tipo: aprendizaje
fecha: 2026-10-21
resumen: El cuello de botella son las GPUs de las laptops, así que el Auto Scaling Group no acelera la inferencia; sirve para demostrar resiliencia.
---
# Aprendizaje: el Auto Scaling no acelera el modelo

- Todas las instancias del ASG mandan la inferencia a las mismas 5 GPUs por Tailscale. Agregar instancias no agrega capacidad de modelo.
- El ASG sirve para **resiliencia**: si una instancia cae, otra retoma el caso desde su checkpoint en PostgreSQL.
- Para ganar velocidad hay que actuar sobre la inferencia: repartir por rol y por caso entre las GPUs, o pasar a un servicio administrado (plan B, Bedrock).
- Configuración propuesta: 2 zonas, mínimo 1 y máximo 3 instancias.
- **Enlaces:** [[tec/data-steward-agentico/arquitectura/_index|arquitectura]], [[tec/data-steward-agentico/arquitectura/decision-monolito-modular|monolito modular]], [[tec/data-steward-agentico/modelos/_index|modelos]]
