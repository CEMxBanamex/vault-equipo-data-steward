---
tipo: aprendizaje
fecha: 2026-10-21
resumen: Ollama no tiene autenticación, así que nunca se expone a internet; solo es alcanzable por Tailscale y con ACL limitadas al puerto 11434.
---
# Aprendizaje: Ollama no tiene autenticación, solo por Tailscale

- Cualquiera que llegue al puerto de Ollama puede usar los modelos. Por eso no se expone a internet ni se abre en el router de nadie.
- Las instancias de EC2 se unen a Tailscale al arrancar con una clave efímera guardada en Secrets Manager.
- Las ACL de Tailscale permiten solo el tráfico de la instancia al puerto `11434` de las laptops.
- El detalle del proceso, reutilizable para otros retos, está en [[tec/_compartido/ollama-gpus-por-tailscale|Ollama en laptops del equipo vía Tailscale]].
- **Enlaces:** [[tec/data-steward-agentico/arquitectura/_index|arquitectura]]
