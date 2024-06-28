import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def grafica_ecuacion_cuadratica_y_derivada(a, b, c):
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.35)  # Ajustar espacio para las cajas de texto

    x = np.linspace(-10, 10, 400)  # Generar 400 puntos igualmente espaciados entre -10 y 10
    y = a * x**2 + b * x + c  # Calcular los valores de y para la ecuación cuadrática
    dy_dx = 2 * a * x + b  # Calcular los valores de y para la derivada

    l, = ax.plot(x, y, lw=2, label='Ecuación Cuadrática', color='blue')  # Dibuja la ecuación cuadrática
    d, = ax.plot(x, dy_dx, lw=2, label='Derivada', color='red')  # Dibuja la derivada

    ax.set_title('Gráfica de la Ecuación Cuadrática y su Derivada')  # Título del gráfico
    ax.set_xlabel('x')  # Etiqueta del eje x
    ax.set_ylabel('y')  # Etiqueta del eje y
    ax.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y=0
    ax.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x=0
    ax.grid(color='gray', linestyle='--', linewidth=0.5)  # Cuadrícula
    ax.legend()  # Mostrar leyenda

    # Definir la posición de las cajas de texto para los coeficientes a, b, y c
    axbox_a = plt.axes([0.1, 0.05, 0.1, 0.075])
    axbox_b = plt.axes([0.3, 0.05, 0.1, 0.075])
    axbox_c = plt.axes([0.5, 0.05, 0.1, 0.075])

    # Crear las cajas de texto
    text_box_a = TextBox(axbox_a, 'a', initial=str(a))
    text_box_b = TextBox(axbox_b, 'b', initial=str(b))
    text_box_c = TextBox(axbox_c, 'c', initial=str(c))

    # Define la función para actualizar la gráfica cuando se cambian los valores en las cajas de texto
    def submit(expression):
        try:
            a = float(text_box_a.text)
            b = float(text_box_b.text)
            c = float(text_box_c.text)
            y = a * x**2 + b * x + c
            dy_dx = 2 * a * x + b
            l.set_ydata(y)  # Actualiza los datos de y para la ecuación cuadrática
            d.set_ydata(dy_dx)  # Actualiza los datos de y para la derivada
            ax.relim()  # Recalcula los límites de los ejes
            ax.autoscale_view()  # Ajusta automáticamente la vista
            plt.draw()  # Redibuja la figura
        except ValueError:
            pass

    # Asocia la función submit con el evento de cambiar texto en las cajas de texto
    text_box_a.on_submit(submit)
    text_box_b.on_submit(submit)
    text_box_c.on_submit(submit)

    plt.show()  # Muestra la figura

# Coeficientes de la ecuación cuadrática inicial
a = 1
b = -3
c = 2

grafica_ecuacion_cuadratica_y_derivada(a, b, c)
