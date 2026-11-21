## Objetivo

Permitir que otra máquina perteneciente al tailnet acceda a Ollama mediante el puerto TCP 11434, sin habilitar el acceso desde redes externas.

## Configuración implementada

- Sistema operativo: Windows.
    
- Servicio: Ollama.
    
- Modelo: `llama3.2:1b`.
    
- IP Tailscale: `100.77.68.53`.
    
- Puerto: `11434/TCP`.
    
- Variable de entorno: `OLLAMA_HOST=100.77.68.53:11434`.
    
- Firewall de Windows: regla de entrada limitada al rango `100.64.0.0/10` y a la interfaz Tailscale.
    

## Evidencias y pruebas

1. Se verificó el funcionamiento local de Ollama mediante `/api/tags`.
    
2. Se comprobó el acceso desde otra computadora conectada al mismo tailnet, obteniendo correctamente el JSON de modelos disponibles.
    
3. Se probó el acceso desde una computadora fuera del tailnet, obteniendo un error de conexión.
    
4. Se verificaron las interfaces de escucha mediante `Get-NetTCPConnection`.
    

## Resultado

Ollama responde mediante la dirección privada de Tailscale y mantiene también su interfaz local de localhost. Las pruebas realizadas confirman el acceso desde un dispositivo del tailnet y el bloqueo desde el dispositivo externo probado.

## Pendiente de documentación de seguridad

Verificar que no existan reglas adicionales de firewall, reenvíos de puertos o mecanismos de exposición pública.
