import tkinter as tk
from tkinter import ttk
import webbrowser
import random

# Función para insertar links de YouTube
def insertar_links():
    for link in [
        "https://www.youtube.com/watch?v=kXYLkE2ZzOU",
        "https://www.youtube.com/watch?v=QA4B7JjQPa8",
        "https://www.youtube.com/watch?v=v-mQm_droHg"
    ]:
        start_index = rutina_text.search(link, "1.0", stopindex=tk.END)
        if start_index:
            end_index = f"{start_index}+{len(link)}c"
            rutina_text.tag_add("link", start_index, end_index)
            rutina_text.tag_configure("link", foreground="blue", underline=True)
            rutina_text.tag_bind("link", "<Button-1>", lambda e, url=link: webbrowser.open(url))

# Función principal para generar la rutina
def generar_rutina():
    try:
        edad = int(edad_entry.get())
    except ValueError:
        rutina_text.delete('1.0', tk.END)
        rutina_text.insert(tk.END, "Por favor ingresa una edad válida.")
        return

    ubicacion = ubicacion_var.get()
    rutina_text.delete('1.0', tk.END)

    if 15 <= edad <= 50:
        if ubicacion == "En casa":
            rutina = """
Rutina en Casa (3 días por semana):

Día 1 - Cuerpo completo
- Sentadillas con peso corporal - 3x15
- Flexiones (push-ups) - 3x10-15
- Remo invertido en mesa - 3x8-12
- Plancha - 3x30 seg

Día 2 - Tren inferior
- Zancadas - 3x12 por pierna
- Puente de glúteos - 3x15
- Subidas a escalón - 3x10 por pierna
- Crunch abdominal - 3x20

Día 3 - Tren superior
- Flexiones con pies elevados - 3x10
- Fondos entre sillas - 3x10
- Curl de bíceps con mochilas - 3x12
- Plancha lateral - 3x30 seg por lado
"""
        elif ubicacion == "Gimnasio":
            rutina = """
Rutina de Gimnasio estilo Jeff Nippard (Push/Pull/Legs - 6 días)

🎥 Enlaces a entrenamientos:
Push: https://www.youtube.com/watch?v=kXYLkE2ZzOU  
Pull: https://www.youtube.com/watch?v=QA4B7JjQPa8  
Piernas: https://www.youtube.com/watch?v=v-mQm_droHg  

Día 1 - Push (Pecho, Hombro, Tríceps)
- Press banca plano con barra – 4x6-8
- Press inclinado con mancuernas – 3x8-10
- Elevaciones laterales – 3x12-15
- Extensiones de tríceps en polea – 3x12-15

Día 2 - Pull (Espalda, Bíceps)
- Peso muerto – 4x6
- Dominadas – 4xAMRAP
- Remo con barra – 3x8-10
- Curl de bíceps con barra – 3x10-12

Día 3 - Piernas
- Sentadilla con barra – 4x6-8
- Prensa de piernas – 3x10-12
- Curl femoral tumbado – 3x12
- Elevación de talones (pantorrilla) – 3x15-20

Día 4 - Push
- Press militar con barra – 4x6-8
- Press banca plano con mancuernas – 3x8-10
- Elevaciones frontales – 3x12
- Fondos en paralelas – 3xAMRAP

Día 5 - Pull
- Jalón al pecho – 4x8-10
- Remo con mancuerna – 3x10-12
- Curl martillo – 3x12
- Face pulls – 3x15

Día 6 - Piernas
- Sentadilla frontal – 4x6-8
- Zancadas con mancuernas – 3x12 por pierna
- Peso muerto rumano – 3x10
- Elevaciones de pantorrillas – 3x20
"""
        else:
            rutina = "Por favor selecciona una ubicación para entrenar."

    elif 60 <= edad <= 70:
        if ubicacion == "En casa":
            rutina = """
Rutina en Casa para Adultos Mayores (60-70 años) - 3 días por semana

Día 1 - Movilidad y fuerza básica
- Marcha en el lugar - 3x1 min
- Sentadillas asistidas (con silla) - 3x10
- Flexiones de pared - 3x10
- Elevación de talones - 3x15

Día 2 - Equilibrio y coordinación
- Caminata de talón a punta - 3x30 seg
- Extensión de pierna sentado - 3x12 por pierna
- Estiramiento de brazos y espalda - 3x30 seg
- Respiración profunda y control postural - 3x1 min

Día 3 - Fuerza general y flexibilidad
- Sentarse y pararse (silla) - 3x10
- Elevación lateral de brazos (botellas pequeñas) - 3x12
- Marcha atrás - 3x30 seg
- Estiramientos suaves (cuádriceps, cuello, hombros) - 3x30 seg
"""
        elif ubicacion == "Gimnasio":
            rutina = """
Rutina de Gimnasio para Adultos Mayores (60-70 años) - 3 días por semana

Día 1 - Tren inferior
- Caminadora o bici estática - 10 minutos
- Prensa de piernas ligera - 3x12
- Extensión de piernas - 3x12
- Elevaciones de talones de pie - 3x15

Día 2 - Tren superior
- Máquina de remo sentado - 3x10
- Press de pecho en máquina - 3x10
- Elevaciones frontales con mancuernas ligeras - 3x12
- Curl de bíceps con mancuernas - 3x12

Día 3 - Full body y movilidad
- Caminata ligera - 10 minutos
- Peso muerto con mancuerna ligera (técnica básica) - 3x8
- Remo con mancuerna - 3x10
- Estiramientos y movilidad articular - 3x1 min
"""
        else:
            rutina = "Por favor selecciona una ubicación para entrenar."
    else:
        rutina = "Lo sentimos, esta app solo ofrece rutinas para edades entre 15 y 50 y 60 a 70 años."

    rutina_text.insert(tk.END, rutina)
    if 15 <= edad <= 50 and ubicacion == "Gimnasio":
        insertar_links()
    notebook.select(frame_rutina)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Generador de Rutinas")
ventana.geometry("700x600")

# Estilos personalizados
style = ttk.Style()
style.configure("Black.TFrame", background="black")

# Crear notebook con pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand=True)

# ASCII decorativo
tiburon_ascii = """
              __
             / _)
     _.----._/ /
    /         /
 __/ (  | (  |
/__.-'|_|--|_|
"""

# Pestaña Bienvenida
frame_bienvenida = ttk.Frame(notebook, style="Black.TFrame")
notebook.add(frame_bienvenida, text='Bienvenida')

tk.Label(frame_bienvenida, text="¡Bienvenido al generador de rutinas!",
         font=("Helvetica", 16), bg="black", fg="white").pack(pady=10)
tk.Label(frame_bienvenida, text="GYM",
         font=("Courier", 24, "bold"), bg="black", fg="yellow").pack(pady=5)
tk.Label(frame_bienvenida, text=tiburon_ascii,
         font=("Courier", 10), bg="black", fg="white", justify="left").pack()
tk.Button(frame_bienvenida, text="Iniciar",
          font=("Helvetica", 14), bg="white", fg="black",
          command=lambda: notebook.select(frame_datos)).pack(pady=20)

# Pestaña Datos del usuario
frame_datos = tk.Frame(notebook, bg="black")
notebook.add(frame_datos, text='Datos del usuario')

labels = ["Edad:", "Peso (kg):", "Sexo:", "Ubicación para entrenar:"]
for i, texto in enumerate(labels):
    tk.Label(frame_datos, text=texto, bg="black", fg="white").grid(row=i, column=0, padx=10, pady=10)

edad_entry = tk.Entry(frame_datos)
edad_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Entry(frame_datos).grid(row=1, column=1, padx=10, pady=10)
ttk.Combobox(frame_datos, values=["Masculino", "Femenino", "Otro"]).grid(row=2, column=1, padx=10, pady=10)

ubicacion_var = tk.StringVar()
ttk.Combobox(frame_datos, textvariable=ubicacion_var, values=["En casa", "Gimnasio"]).grid(row=3, column=1, padx=10, pady=10)

tk.Button(frame_datos, text="Generar rutina", command=generar_rutina).grid(row=4, columnspan=2, pady=10)

for _ in range(5):
    r = random.randint(5, 10)
    c = random.randint(0, 1)
    tk.Label(frame_datos, text="gym", bg="black", fg="yellow", font=("Courier", 10)).grid(row=r, column=c, padx=5, pady=5)

# Pestaña Rutina
frame_rutina = tk.Frame(notebook, bg="black")
notebook.add(frame_rutina, text='Tu rutina')

rutina_text = tk.Text(frame_rutina, wrap=tk.WORD, font=("Helvetica", 12), bg="black", fg="white", insertbackground="white")
rutina_text.pack(padx=10, pady=10, fill='both', expand=True)

for _ in range(5):
    label = tk.Label(frame_rutina, text="gym", fg="yellow", bg="black", font=("Courier", 10))
    x = random.randint(0, 600)
    y = random.randint(0, 500)
    label.place(x=x, y=y)

# Navegación con Enter
ventana.bind('<Return>', lambda event: (
    notebook.select(frame_datos) if notebook.index(notebook.select()) == 0 else (
        notebook.select(frame_rutina) if notebook.index(notebook.select()) == 1 else None
    )
))

ventana.mainloop()
            
