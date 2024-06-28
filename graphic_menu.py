import numpy as np  # Importa la biblioteca numpy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para crear gráficos
from matplotlib.widgets import TextBox, Button  # Importa widgets de matplotlib para añadir interactividad

# Función para graficar una ecuación cuadrática
def grafica_ecuacion_cuadratica(ax, a, b, c):
    x = np.linspace(-10, 10, 400)  # Genera 400 puntos igualmente espaciados entre -10 y 10
    y = a * x**2 + b * x + c  # Calcula los valores de y para la ecuación cuadrática
    dy_dx = 2 * a * x + b  # Calcula los valores de y para la derivada
    ax.clear()  # Limpia la gráfica actual
    ax.plot(x, y, lw=2, label='Ecuación Cuadrática', color='blue')  # Dibuja la ecuación cuadrática
    ax.plot(x, dy_dx, lw=2, label='Derivada', color='red')  # Dibuja la derivada
    ax.set_title('Ecuación Cuadrática y su Derivada')  # Establece el título del gráfico
    ax.set_xlabel('x')  # Establece la etiqueta del eje x
    ax.set_ylabel('y')  # Establece la etiqueta del eje y
    ax.axhline(0, color='black', linewidth=0.5)  # Dibuja la línea horizontal en y=0
    ax.axvline(0, color='black', linewidth=0.5)  # Dibuja la línea vertical en x=0
    ax.grid(color='gray', linestyle='--', linewidth=0.5)  # Dibuja la cuadrícula
    ax.legend()  # Muestra la leyenda
    plt.draw()  # Redibuja la figura

# Función para graficar una línea recta
def grafica_linea_recta(ax, m, b):
    x = np.linspace(-10, 10, 400)  # Genera 400 puntos igualmente espaciados entre -10 y 10
    y = m * x + b  # Calcula los valores de y para la línea recta
    ax.clear()  # Limpia la gráfica actual
    ax.plot(x, y, lw=2, label='Línea Recta', color='blue')  # Dibuja la línea recta
    ax.set_title('Línea Recta')  # Establece el título del gráfico
    ax.set_xlabel('x')  # Establece la etiqueta del eje x
    ax.set_ylabel('y')  # Establece la etiqueta del eje y
    ax.axhline(0, color='black', linewidth=0.5)  # Dibuja la línea horizontal en y=0
    ax.axvline(0, color='black', linewidth=0.5)  # Dibuja la línea vertical en x=0
    ax.grid(color='gray', linestyle='--', linewidth=0.5)  # Dibuja la cuadrícula
    ax.legend()  # Muestra la leyenda
    plt.draw()  # Redibuja la figura

# Función para graficar una ecuación cúbica
def grafica_ecuacion_cubica(ax, a, b, c, d):
    x = np.linspace(-10, 10, 400)  # Genera 400 puntos igualmente espaciados entre -10 y 10
    y = a * x**3 + b * x**2 + c * x + d  # Calcula los valores de y para la ecuación cúbica
    dy_dx = 3 * a * x**2 + 2 * b * x + c  # Calcula los valores de y para la derivada
    ax.clear()  # Limpia la gráfica actual
    ax.plot(x, y, lw=2, label='Ecuación Cúbica', color='blue')  # Dibuja la ecuación cúbica
    ax.plot(x, dy_dx, lw=2, label='Derivada', color='red')  # Dibuja la derivada
    ax.set_title('Ecuación Cúbica y su Derivada')  # Establece el título del gráfico
    ax.set_xlabel('x')  # Establece la etiqueta del eje x
    ax.set_ylabel('y')  # Establece la etiqueta del eje y
    ax.axhline(0, color='black', linewidth=0.5)  # Dibuja la línea horizontal en y=0
    ax.axvline(0, color='black', linewidth=0.5)  # Dibuja la línea vertical en x=0
    ax.grid(color='gray', linestyle='--', linewidth=0.5)  # Dibuja la cuadrícula
    ax.legend()  # Muestra la leyenda
    plt.draw()  # Redibuja la figura

# Función para actualizar la gráfica según los coeficientes ingresados
def update_graph(event):
    a = float(text_box_a.text) if text_box_a.text else 0  # Obtiene el valor de a de la caja de texto
    b = float(text_box_b.text) if text_box_b.text else 0  # Obtiene el valor de b de la caja de texto
    c = float(text_box_c.text) if text_box_c.text else 0  # Obtiene el valor de c de la caja de texto
    d = float(text_box_d.text) if text_box_d.text else 0  # Obtiene el valor de d de la caja de texto
    
    if equation_type == 'cuadratica':
        grafica_ecuacion_cuadratica(ax, a, b, c)  # Llama a la función para graficar la ecuación cuadrática
    elif equation_type == 'recta':
        grafica_linea_recta(ax, a, b)  # Llama a la función para graficar la línea recta
    elif equation_type == 'cubica':
        grafica_ecuacion_cubica(ax, a, b, c, d)  # Llama a la función para graficar la ecuación cúbica

# Funciones para configurar el tipo de ecuación
def set_cuadratica(event):
    global equation_type
    equation_type = 'cuadratica'  # Establece el tipo de ecuación como cuadrática
    ax.clear()  # Limpia la gráfica actual
    ax.set_title('Ecuación Cuadrática y su Derivada')  # Establece el título del gráfico
    plt.draw()  # Redibuja la figura

def set_recta(event):
    global equation_type
    equation_type = 'recta'  # Establece el tipo de ecuación como línea recta
    ax.clear()  # Limpia la gráfica actual
    ax.set_title('Línea Recta')  # Establece el título del gráfico
    plt.draw()  # Redibuja la figura

def set_cubica(event):
    global equation_type
    equation_type = 'cubica'  # Establece el tipo de ecuación como cúbica
    ax.clear()  # Limpia la gráfica actual
    ax.set_title('Ecuación Cúbica y su Derivada')  # Establece el título del gráfico
    plt.draw()  # Redibuja la figura

# Configuración inicial de la figura y los ejes
fig, ax = plt.subplots()  # Crea una figura y un conjunto de ejes
plt.subplots_adjust(top=0.95, bottom=0.4)  # Ajusta el espacio en la parte inferior para las cajas de texto y botones
ax.set_title('Seleccione el tipo de ecuación y ajuste los coeficientes')  # Establece el título inicial del gráfico

# Botones de selección de tipo de ecuación
ax_button_cuadratica = plt.axes([0.1, 0.25, 0.2, 0.075])  # Define la posición y tamaño del botón cuadrática
button_cuadratica = Button(ax_button_cuadratica, 'Cuadrática')  # Crea el botón para seleccionar la ecuación cuadrática
button_cuadratica.on_clicked(set_cuadratica)  # Asocia la función set_cuadratica con el botón

ax_button_recta = plt.axes([0.4, 0.25, 0.2, 0.075])  # Define la posición y tamaño del botón recta
button_recta = Button(ax_button_recta, 'Línea Recta')  # Crea el botón para seleccionar la línea recta
button_recta.on_clicked(set_recta)  # Asocia la función set_recta con el botón

ax_button_cubica = plt.axes([0.7, 0.25, 0.2, 0.075])  # Define la posición y tamaño del botón cúbica
button_cubica = Button(ax_button_cubica, 'Cúbica')  # Crea el botón para seleccionar la ecuación cúbica
button_cubica.on_clicked(set_cubica)  # Asocia la función set_cubica con el botón

# Cajas de texto para los coeficientes
axbox_a = plt.axes([0.1, 0.05, 0.1, 0.075])  # Define la posición y tamaño de la caja de texto para a
text_box_a = TextBox(axbox_a, 'a', initial="0")  # Crea la caja de texto para el coeficiente a

axbox_b = plt.axes([0.3, 0.05, 0.1, 0.075])  # Define la posición y tamaño de la caja de texto para b
text_box_b = TextBox(axbox_b, 'b', initial="0")  # Crea la caja de texto para el coeficiente b

axbox_c = plt.axes([0.5, 0.05, 0.1, 0.075])  # Define la posición y tamaño de la caja de texto para c
text_box_c = TextBox(axbox_c, 'c', initial="0")  # Crea la caja de texto para el coeficiente c

axbox_d = plt.axes([0.7, 0.05, 0.1, 0.075])  # Define la posición y tamaño de la caja de texto para d
text_box_d = TextBox(axbox_d, 'd', initial="0")  # Crea la caja de texto para el coeficiente d

# Botón para actualizar la gráfica
ax_button_update = plt.axes([0.4, 0.15, 0.2, 0.075])  # Define la posición y tamaño del botón actualizar
button_update = Button(ax_button_update, 'Actualizar')  # Crea el botón para actualizar la gráfica
button_update.on_clicked(update_graph)  # Asocia la función update_graph con el botón

# Variable global para almacenar el tipo de ecuación seleccionado
equation_type = 'cuadratica'  # Inicializa el tipo de ecuación como cuadrática

plt.show()  # Muestra la figura
