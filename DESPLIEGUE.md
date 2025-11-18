# Guía de Despliegue en Heroku

## Pasos para publicar tu calculadora:

### 1. Preparación (ya hecho ✅)
- requirements.txt creado
- Procfile creado  
- web_app.py configurado para producción

### 2. Instalar Heroku CLI
- Descargar de: https://devcenter.heroku.com/articles/heroku-cli
- Instalar en tu sistema

### 3. Comandos para desplegar:

```bash
# Inicializar git (si no tienes)
git init
git add .
git commit -m "Calculadora rifles de aire PCP"

# Login a Heroku
heroku login

# Crear aplicación
heroku create tu-calculadora-rifles-aire

# Desplegar
git push heroku main

# Ver la app
heroku open
```

### 4. Tu app estará disponible en:
https://tu-calculadora-rifles-aire.herokuapp.com

## Alternativas Adicionales:

### Railway.app (Muy fácil)
1. Conectar tu GitHub
2. Despliegue automático
3. URL pública instantánea

### Render.com (Gratuito)
1. Conectar repositorio
2. Detección automática de Flask
3. Despliegue sin configuración

### PythonAnywhere (Simple)
1. Subir archivos
2. Configurar WSGI
3. Dominio gratuito incluido

### Vercel (Rápido)
1. Conectar GitHub
2. Despliegue automático
3. CDN global incluido

## Recomendación:
**Heroku** es la opción más fácil para empezar. 
Si quieres algo más moderno, usa **Railway.app** o **Render.com**.