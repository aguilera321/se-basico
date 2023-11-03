base_de_conocimiento = {
    'italiana': ['pizza', 'pasta'],  # Recomendaciones de comida italiana
    'mexicana': ['tacos', 'enchiladas'],  # Recomendaciones de comida mexicana
    'japonesa': ['sushi', 'ramen'],  # Recomendaciones de comida japonesa
    'india': ['curry', 'naan'],  # Recomendaciones de comida india
    'paraguaya': ['vori vori', 'chipa guazu'] # Recomendaciones de comida paraguaya
}

# Función del motor de inferencia
def motor_de_inferencia(tipo_comida):
    if tipo_comida in base_de_conocimiento:  # Verifica si el tipo de comida está en la base de conocimiento
        return base_de_conocimiento[tipo_comida]  # Devuelve las recomendaciones correspondientes al tipo de comida ingresado
    else:
        return ['No se encontraron recomendaciones para este tipo de comida']  # Mensaje de error si el tipo de comida no está en la base de conocimiento
    
import tkinter as tk  # Importa la biblioteca Tkinter para crear la interfaz gráfica

# Función para mostrar las recomendaciones
def mostrar_recomendaciones():
    tipo_comida = entrada.get().lower()  # Obtiene el tipo de comida ingresado y lo convierte a minúsculas
    recomendaciones = motor_de_inferencia(tipo_comida)  # Llama a la función de motor de inferencia para obtener recomendaciones
    resultado.config(text="Recomendaciones de comida: " + ', '.join(recomendaciones))  # Actualiza la etiqueta de resultado con las recomendaciones

# Función para borrar el texto del campo de entrada y el texto de recomendaciones
def borrar_texto():
    entrada.delete(0, tk.END)
    resultado.config(text="")

app = tk.Tk()  # Crea una ventana de Tkinter
app.title("Sistema Experto - recomendaciones de comidas basadas en el tipo de comida que te gusta")  # Establece el título de la ventana
app.geometry("500x200")  # Establece el tamaño inicial de la ventana en 300x200 píxeles
app.resizable(False, False)  # Evita que la ventana se pueda redimensionar y maximizar

# Cambiar el icono de la ventana
app.iconbitmap("icon.ico")  # Reemplaza "icon.ico" con la ruta de tu propio archivo de icono

etiqueta = tk.Label(app, text="Ingresa el tipo de comida que te guste (italiana, mexicana, japonesa, india o paraguaya):")  # Crea una etiqueta de texto
etiqueta.pack(pady=10)  # Coloca la etiqueta en la ventana con un espacio en la parte superior

entrada = tk.Entry(app)  # Crea un campo de entrada de texto
entrada.pack(pady=5)  # Coloca el campo de entrada en la ventana con un espacio en la parte superior

boton = tk.Button(app, text="Obtener Recomendaciones", command=mostrar_recomendaciones, bg="lightblue")  # Crea un botón
boton.pack(pady=10)  # Coloca el botón en la ventana con un espacio en la parte superior

# Agrega un botón para borrar el texto del campo de entrada y el texto de recomendaciones
boton_borrar = tk.Button(app, text="Borrar", command=borrar_texto, bg="red")
boton_borrar.pack()

resultado = tk.Label(app, text="", font=("Helvetica", 12), fg="blue")  # Crea una etiqueta para mostrar resultados
resultado.pack()  # Coloca la etiqueta en la ventana

app.mainloop()  # Inicia el bucle principal de la aplicación para mostrar la ventana y manejar eventos