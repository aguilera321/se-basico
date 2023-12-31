# Sistema Experto Básico - Recomendaciones según el tipo de comida

Este es un Sistema Experto básico desarrollado en Python que recomienda comidas según el pais. El sistema incluye una base de conocimiento, un motor de inferencia y una interfaz gráfica simple.

## Requisitos

- Python 3.x instalado en tu sistema.
- La biblioteca Tkinter para la interfaz gráfica. En la mayoría de los sistemas, Tkinter ya está incluido con la instalación de Python.

## Ejecución

1. Clona este repositorio en tu máquina local o descárgalo como un archivo ZIP.
2. Abre una terminal o línea de comandos y navega al directorio donde se encuentra el código del proyecto.
3. Ejecuta el programa con el siguiente comando: python sistema_experto.py
Asegúrate de que el archivo Python tenga el nombre `sistema_experto.py` o cámbialo según tu conveniencia.

4. La aplicación de la interfaz gráfica se abrirá. Ingrese el tipo de comida (italiana, mexicana, japonesa, india o paraguaya) y haga clic en el botón "Obtener Recomendaciones". Las recomendaciones se mostrarán en la ventana.

## Base de Conocimiento y Motor de Inferencia

El sistema utiliza una base de conocimiento predefinida en forma de reglas en un diccionario Python. El motor de inferencia consulta esta base de conocimiento para determinar las recomendaciones según el clima ingresado.

```python
base_de_conocimiento = {
    'italiana': ['pizza', 'pasta'],  # Recomendaciones de comida italiana
    'mexicana': ['tacos', 'enchiladas'],  # Recomendaciones de comida mexicana
    'japonesa': ['sushi', 'ramen'],  # Recomendaciones de comida japonesa
    'india': ['curry', 'naan'],  # Recomendaciones de comida india
    'paraguaya': ['vori vori', 'chipa guazu'] # Recomendaciones de comida paraguaya
}
