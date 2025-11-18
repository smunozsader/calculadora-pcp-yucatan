from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def calcular_energia_cinetica(masa_granos, velocidad_fps):
    """Calcula la energía cinética en joules"""
    masa_kg = masa_granos * 0.0000647989  # granos a kilogramos
    velocidad_ms = velocidad_fps * 0.3048  # fps a m/s
    energia_joules = 0.5 * masa_kg * (velocidad_ms ** 2)
    return energia_joules

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        data = request.get_json()
        peso = float(data['peso'])
        velocidad = float(data['velocidad'])
        
        if peso <= 0 or velocidad <= 0:
            return jsonify({'error': 'Los valores deben ser positivos'}), 400
        
        energia = calcular_energia_cinetica(peso, velocidad)
        requiere_registro = energia > 140
        
        resultado = {
            'energia': round(energia, 2),
            'requiere_registro': requiere_registro,
            'diferencia': round(abs(energia - 140), 2),
            'mensaje': '⚠️ REQUIERE REGISTRO' if requiere_registro else '✅ NO REQUIERE REGISTRO',
            'detalle': f'Excede el límite por {energia - 140:.2f} joules' if requiere_registro 
                      else f'Está {140 - energia:.2f} joules por debajo del límite'
        }
        
        return jsonify(resultado)
        
    except (ValueError, KeyError) as e:
        return jsonify({'error': 'Datos inválidos'}), 400

@app.route('/tabla-referencia')
def tabla_referencia():
    calibres = {
        # Calibres Pequeños - Target & Pest Control
        ".177 (4.5mm)": 8.2,
        ".20 (5.0mm)": 12.0,
        ".22 (5.5mm)": 14.3,
        ".22 (5.6mm)": 15.0,
        
        # Calibres Medianos - Small to Medium Game
        ".25 (6.35mm)": 25.4,
        ".30 (7.62mm)": 44.8,
        
        # Calibres Grandes - Big Game Hunting
        ".357 (9.07mm)": 81.0,
        ".45 (11.43mm)": 143.0,
        ".50 (12.7mm)": 178.0
    }
    
    tabla = []
    for calibre, peso in calibres.items():
        masa_kg = peso * 0.0000647989
        v_ms_limite = math.sqrt(2 * 140 / masa_kg)
        v_fps_limite = v_ms_limite / 0.3048
        
        tabla.append({
            'calibre': calibre,
            'peso': peso,
            'velocidad_limite': round(v_fps_limite, 0)
        })
    
    return jsonify(tabla)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    
    # Configuración inteligente: debug solo en desarrollo
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    
    if debug_mode:
        print("🚀 Iniciando servidor Flask en modo desarrollo...")
        print("📍 Accede a: http://localhost:5000")
        print("🔄 Presiona Ctrl+C para detener")
    else:
        print("🌐 Iniciando servidor Flask en modo producción...")
    
    app.run(debug=debug_mode, host='0.0.0.0', port=port)