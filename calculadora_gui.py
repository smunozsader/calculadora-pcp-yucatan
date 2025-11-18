import tkinter as tk
from tkinter import ttk, messagebox
import math

class CalculadoraRiflesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Registro - Rifles PCP México")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Configurar estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(main_frame, text="Calculadora de Registro de Rifles PCP - México", 
                               font=('Arial', 14, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        subtitle_label = ttk.Label(main_frame, text="Límite legal: 140 joules", 
                                  font=('Arial', 10, 'italic'))
        subtitle_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Calibre
        ttk.Label(main_frame, text="Calibre:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.calibre_var = tk.StringVar()
        calibre_combo = ttk.Combobox(main_frame, textvariable=self.calibre_var, 
                                    values=["4.5mm (.177)", "5.0mm (.20)", "5.5mm (.22)", "6.35mm (.25)"],
                                    state="readonly", width=20)
        calibre_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        calibre_combo.bind('<<ComboboxSelected>>', self.on_calibre_change)
        
        # Peso del proyectil
        ttk.Label(main_frame, text="Peso (granos):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.peso_var = tk.StringVar()
        self.peso_entry = ttk.Entry(main_frame, textvariable=self.peso_var, width=20)
        self.peso_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Velocidad
        ttk.Label(main_frame, text="Velocidad (fps):").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.velocidad_var = tk.StringVar()
        velocidad_entry = ttk.Entry(main_frame, textvariable=self.velocidad_var, width=20)
        velocidad_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Botón calcular
        calcular_btn = ttk.Button(main_frame, text="Calcular", command=self.calcular)
        calcular_btn.grid(row=5, column=0, columnspan=2, pady=20)
        
        # Frame de resultados
        self.resultado_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="15")
        self.resultado_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Labels de resultados
        self.energia_label = ttk.Label(self.resultado_frame, text="", font=('Arial', 12))
        self.energia_label.grid(row=0, column=0, pady=5)
        
        self.status_label = ttk.Label(self.resultado_frame, text="", font=('Arial', 12, 'bold'))
        self.status_label.grid(row=1, column=0, pady=5)
        
        self.diferencia_label = ttk.Label(self.resultado_frame, text="")
        self.diferencia_label.grid(row=2, column=0, pady=5)
        
        # Botón tabla de referencia
        tabla_btn = ttk.Button(main_frame, text="Ver Tabla de Referencia", command=self.mostrar_tabla)
        tabla_btn.grid(row=7, column=0, columnspan=2, pady=10)
        
        # Configurar grid weights
        main_frame.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
    def on_calibre_change(self, event=None):
        """Actualiza el peso promedio cuando se cambia el calibre"""
        calibres_datos = {
            "4.5mm (.177)": 8.2,
            "5.0mm (.20)": 12.0,
            "5.5mm (.22)": 14.3,
            "6.35mm (.25)": 25.4
        }
        calibre_seleccionado = self.calibre_var.get()
        if calibre_seleccionado in calibres_datos:
            self.peso_var.set(str(calibres_datos[calibre_seleccionado]))
    
    def calcular_energia_cinetica(self, masa_granos, velocidad_fps):
        """Calcula la energía cinética en joules"""
        masa_kg = masa_granos * 0.0000647989  # granos a kilogramos
        velocidad_ms = velocidad_fps * 0.3048  # fps a m/s
        energia_joules = 0.5 * masa_kg * (velocidad_ms ** 2)
        return energia_joules
    
    def calcular(self):
        try:
            peso = float(self.peso_var.get())
            velocidad = float(self.velocidad_var.get())
            
            if peso <= 0 or velocidad <= 0:
                messagebox.showerror("Error", "Los valores deben ser positivos")
                return
                
            energia = self.calcular_energia_cinetica(peso, velocidad)
            
            # Actualizar resultados
            self.energia_label.config(text=f"Energía: {energia:.2f} joules")
            
            if energia > 140:
                self.status_label.config(text="⚠️ REQUIERE REGISTRO", foreground="red")
                self.diferencia_label.config(text=f"Excede el límite por {energia - 140:.2f} joules")
            else:
                self.status_label.config(text="✅ NO REQUIERE REGISTRO", foreground="green")
                self.diferencia_label.config(text=f"Está {140 - energia:.2f} joules por debajo del límite")
                
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")
    
    def mostrar_tabla(self):
        """Muestra ventana con tabla de referencia"""
        tabla_window = tk.Toplevel(self.root)
        tabla_window.title("Tabla de Referencia")
        tabla_window.geometry("500x400")
        
        frame = ttk.Frame(tabla_window, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Velocidades Límite por Calibre", 
                 font=('Arial', 14, 'bold')).pack(pady=(0, 20))
        
        # Crear tabla
        tree = ttk.Treeview(frame, columns=('Calibre', 'Peso', 'Vel_Limite'), show='headings')
        tree.heading('Calibre', text='Calibre')
        tree.heading('Peso', text='Peso (granos)')
        tree.heading('Vel_Limite', text='Velocidad Límite (fps)')
        
        calibres = {
            "4.5mm (.177)": 8.2,
            "5.0mm (.20)": 12.0,
            "5.5mm (.22)": 14.3,
            "6.35mm (.25)": 25.4
        }
        
        for calibre, peso in calibres.items():
            masa_kg = peso * 0.0000647989
            v_ms_limite = math.sqrt(2 * 140 / masa_kg)
            v_fps_limite = v_ms_limite / 0.3048
            
            tree.insert('', 'end', values=(calibre, peso, f"{v_fps_limite:.0f}"))
        
        tree.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        info_label = ttk.Label(frame, text="Nota: Velocidades superiores requieren registro según ley mexicana",
                              font=('Arial', 9, 'italic'))
        info_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraRiflesGUI(root)
    root.mainloop()