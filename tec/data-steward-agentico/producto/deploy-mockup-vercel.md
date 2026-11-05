---
tipo: aprendizaje
fecha: 2026-10-28
resumen: El mockup está desplegado en Vercel desde la carpeta frontend del monorepo; el repo vive en la organización de GitHub, así que Vercel necesita acceso a ella.
---
# Aprendizaje: deploy del mockup en Vercel

- **URL:** https://banamex-cem.vercel.app/ (pública; todos los datos son ficticios).
- **Origen:** el monorepo vive en la **organización** de GitHub del equipo, no en la cuenta personal. Por eso no aparecía en **Import Git Repository**: hay que cambiar de cuenta en el selector o instalar la app de Vercel en la organización (si no eres admin, un admin aprueba la solicitud).
- **Configuración del proyecto:**
  - **Root Directory: `frontend`.** Es lo importante: el `package.json` no está en la raíz del repo y, sin esto, el build falla.
  - Framework Vite (se detecta solo), build `npm run build`, salida `dist`.
  - Sin variables de entorno: el mockup no tiene conexiones.
- **Redeploy:** cada push a `main` vuelve a desplegar.
- **Cuidado:** la URL es pública y muestra la marca del socio. Si no debe verla cualquiera, activar **Deployment Protection** (inicio de sesión en Vercel o contraseña, esta última solo en planes de pago).
- **Enlaces:** [[tec/data-steward-agentico/producto/mockup-interfaz|Mockup navegable de la interfaz]], [[tec/data-steward-agentico/producto/_index|producto]]
