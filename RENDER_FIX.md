🚨 **CONFIGURACIÓN MANUAL EN RENDER.COM**

**PASO 1: Ve a tu Dashboard de Render**
1. Entra a: https://dashboard.render.com
2. Busca: `calculadora-pcp-yucatan`
3. Click en el servicio

**PASO 2: Editar Configuración**
1. Click **"Settings"** (⚙️)
2. Scroll hasta **"Build & Deploy"**
3. En **"Start Command"** cambiar de:
   ```
   gunicorn app:app
   ```
   A:
   ```
   gunicorn web_app:app
   ```

**PASO 3: Aplicar Cambios**
1. Click **"Save Changes"**
2. El servicio se redesplegará automáticamente
3. ⏱️ Espera 2-3 minutos

**ALTERNATIVA RÁPIDA:**
También puedes hacer "Manual Deploy" desde el botón en la esquina superior derecha.

---

**✅ DESPUÉS VERÁS EN LOS LOGS:**
```
==> Running 'gunicorn web_app:app'  ← CORRECTO
[INFO] Starting gunicorn 21.2.0
[INFO] Listening at: http://0.0.0.0:10000
✅ Deploy successful
```

**🌐 URL FINAL:**
https://calculadora-pcp-yucatan.onrender.com