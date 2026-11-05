---
tipo: ficha
subtipo: proceso
revisado: 2026-10-21
usada-en: [data-steward-agentico]
resumen: Cómo usar las laptops con GPU del equipo como servidores de inferencia con Ollama, alcanzables desde la nube solo por Tailscale.
---
# Ollama en laptops del equipo vía Tailscale

- **Qué es:** patrón para retos sin presupuesto de GPU en la nube. Cada laptop del equipo corre Ollama con sus modelos en disco, y las instancias en la nube llegan a ellas por una red privada de Tailscale. Los modelos no se despliegan en la nube.
- **Ambientes:** una tailnet del equipo. Cada laptop es un nodo; cada instancia de la nube se une como nodo efímero al arrancar.
- **Cómo se obtiene acceso:**
  - Cada integrante instala Tailscale y Ollama en su laptop y se une a la tailnet del equipo.
  - Las instancias se unen al arrancar con una **clave efímera** guardada en el gestor de secretos de la nube (en AWS, Secrets Manager), nunca en el repo ni en la imagen.
  - Las **ACL** de Tailscale permiten solo el tráfico de las instancias al puerto `11434` (Ollama) de las laptops.
- **Reparto del trabajo:**
  - Por rol: una laptop por tipo de modelo (por ejemplo, visión, razonamiento, embeddings y respaldo), según la VRAM de cada GPU.
  - En evaluaciones por lote, también por caso.
  - Fijar la etiqueta exacta de cada modelo en Ollama.
- **Dueño:** el equipo del reto.
- **Gotchas:**
  - **Ollama no tiene autenticación.** Nunca exponerlo a internet; solo debe ser alcanzable por Tailscale.
  - Si una laptop se apaga o se duerme, su rol se cae: tener un nodo de respaldo.
  - El cuello de botella son las GPUs. Escalar instancias en la nube no acelera la inferencia.
  - El modelo de embeddings tiene que ser el mismo al indexar y al consultar.
  - Revisar los límites del plan gratuito de Tailscale (usuarios y dispositivos) antes de depender de él.
  - Plan B si la calidad o la disponibilidad no alcanzan: un servicio administrado (por ejemplo, Amazon Bedrock).
