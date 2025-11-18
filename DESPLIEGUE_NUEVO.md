# 🚀 GUÍA COMPLETA DE DESPLIEGUE - Calculadora PCP

## 📋 **MÉTODO RECOMENDADO: RENDER.COM (100% GRATIS)**

### 🎯 **¿Por qué Render.com?**
- ✅ **750 horas gratis al mes** (suficiente para uso continuo)
- ✅ **SSL automático** (HTTPS seguro)
- ✅ **Dominio gratuito** (.onrender.com)
- ✅ **Despliegue automático** desde GitHub
- ✅ **Sin tarjeta de crédito** requerida

---

## 🚀 **PASO A PASO - DESPLIEGUE EN 10 MINUTOS**

### **PASO 1: Crear cuenta en GitHub** (si no tienes)
1. Ve a [github.com](https://github.com)
2. Clic en "Sign up" 
3. Crea tu cuenta gratuita

### **PASO 2: Subir tu proyecto a GitHub**
1. Ve a [github.com/new](https://github.com/new)
2. Nombre del repositorio: `calculadora-pcp-club`
3. Descripción: `Calculadora de Energía PCP - Club de Caza Yucatán`
4. Público ✅ (para plan gratuito)
5. Clic **"Create repository"**

### **PASO 3: Subir archivos** 
En la página del repositorio nuevo:
1. Clic **"uploading an existing file"**
2. Arrastra TODOS estos archivos:
   ```
   📁 Mi proyecto/
   ├── web_app.py
   ├── requirements.txt  
   ├── Procfile
   ├── templates/index.html
   └── static/
       ├── logo-club.jpg
       └── femeti-logo.avif
   ```
3. Mensaje: `Initial upload - Calculadora PCP Club Yucatán`
4. Clic **"Commit changes"**

### **PASO 4: Crear cuenta en Render.com**
1. Ve a [render.com](https://render.com)
2. Clic **"Get Started for Free"**
3. **Registrate con GitHub** (más fácil)
4. Autoriza la conexión

### **PASO 5: Crear Web Service**
1. En el dashboard de Render, clic **"New +"**
2. Selecciona **"Web Service"**
3. Clic **"Connect GitHub account"** (si no está conectado)
4. Busca y selecciona tu repositorio `calculadora-pcp-club`
5. Clic **"Connect"**

### **PASO 6: Configuración del servicio**
```
Name: calculadora-pcp-yucatan
Region: Oregon (US West)
Branch: main
Root Directory: (dejar vacío)
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn web_app:app
```

### **PASO 7: Plan gratuito**
- Plan: **Free** ✅
- Clic **"Create Web Service"**

### **PASO 8: ¡Esperar el despliegue!**
- Render automáticamente:
  - ⬇️ Descarga tu código
  - 🐍 Instala Python y dependencias  
  - 🚀 Inicia tu aplicación
  - 🌐 Te da una URL pública

---

## 🎉 **¡LISTO! Tu aplicación estará en:**
```
https://calculadora-pcp-yucatan.onrender.com
```

---

## 🔧 **CONFIGURACIONES AVANZADAS (OPCIONAL)**

### **Dominio Personalizado**
Si quieres un dominio como `calculadora-pcp.com`:
1. Compra el dominio en Namecheap (~$10/año)
2. En Render: Settings → Custom Domains
3. Agrega tu dominio
4. Configura DNS según instrucciones

### **Variables de Entorno** 
Tu app YA está optimizada para producción:
- ✅ Debug mode OFF automáticamente
- ✅ Puerto asignado dinámicamente  
- ✅ Headers anti-caché configurados

### **Actualizaciones Automáticas**
Cada vez que subas cambios a GitHub:
1. Ve a tu repositorio
2. Clic en el archivo a editar
3. Haz cambios
4. "Commit changes"
5. **Render detecta y re-despliega automáticamente** 🤖

---

## 📊 **ALTERNATIVAS GRATUITAS**

### **Railway.app** (Alternativa #2)
- 500 horas gratis/mes
- Proceso similar a Render
- Registro en [railway.app](https://railway.app)

### **Vercel** (Alternativa #3)  
- Para aplicaciones estáticas principalmente
- Excelente para Next.js/React

---

## 🆘 **SOLUCIÓN DE PROBLEMAS**

### **Error: "Build failed"**
- Verifica que `requirements.txt` esté en la raíz
- Revisa que `Procfile` tenga: `web: gunicorn web_app:app`

### **Error: "Application failed to start"**
- En Render logs, busca errores específicos
- Verifica que el archivo principal sea `web_app.py`

### **La página no carga logos**
- Verifica que `static/` contenga los archivos `.jpg` y `.avif`
- Revisa que los nombres coincidan exactamente

### **Rendimiento lento**
- Plan gratuito "duerme" después de 15 min sin uso
- Primera carga después del sueño toma ~30 segundos
- Usuarios subsecuentes: carga normal

---

## 📞 **CONTACTO TÉCNICO**
Si necesitas ayuda con el despliegue:
- WhatsApp Club: +52 56 6582 4667
- Facebook: Club de Caza, Tiro y Pesca de Yucatán

---

## ⚡ **RESUMEN RÁPIDO**
1. **GitHub** → Sube código
2. **Render.com** → Conecta repositorio  
3. **Configurar** → Python + gunicorn
4. **Desplegar** → ¡Automático!
5. **Compartir** → URL pública lista

**Tiempo total: ~10 minutos** ⏱️