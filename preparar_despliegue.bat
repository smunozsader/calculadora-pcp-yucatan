@echo off
echo 🚀 PREPARANDO ARCHIVOS PARA DESPLIEGUE...
echo.

echo ✅ Verificando estructura de archivos...
if not exist "web_app.py" (
    echo ❌ ERROR: web_app.py no encontrado
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo ❌ ERROR: requirements.txt no encontrado  
    pause
    exit /b 1
)

if not exist "Procfile" (
    echo ❌ ERROR: Procfile no encontrado
    pause
    exit /b 1
)

if not exist "templates\index.html" (
    echo ❌ ERROR: templates/index.html no encontrado
    pause
    exit /b 1
)

if not exist "static\logo-club.jpg" (
    echo ⚠️  ADVERTENCIA: static/logo-club.jpg no encontrado
)

if not exist "static\femeti-logo.avif" (
    echo ⚠️  ADVERTENCIA: static/femeti-logo.avif no encontrado
)

echo.
echo ✅ Archivos principales verificados
echo.
echo 📋 ARCHIVOS LISTOS PARA GITHUB:
echo    ├── web_app.py
echo    ├── requirements.txt  
echo    ├── Procfile
echo    ├── README.md
echo    ├── DESPLIEGUE.md
echo    ├── .gitignore
echo    ├── templates/
echo    │   └── index.html
echo    └── static/
echo        ├── logo-club.jpg
echo        └── femeti-logo.avif
echo.
echo 🎯 PRÓXIMOS PASOS:
echo    1. Ve a: https://github.com/new
echo    2. Nombre: calculadora-pcp-club  
echo    3. Sube estos archivos (drag & drop)
echo    4. Ve a: https://render.com
echo    5. Conecta tu repositorio GitHub
echo    6. ¡Despliegue automático!
echo.
echo 📖 Lee DESPLIEGUE.md para instrucciones detalladas
echo.
pause