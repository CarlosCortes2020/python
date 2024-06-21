import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def grafica_ecuacion_cuadratica(a, b, c):
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    l, = plt.plot(x, y, lw=2)
    plt.title('Gráfica de la Ecuación Cuadrática')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    
    # Definir la posición de las cajas de texto
    axbox_a = plt.axes([0.1, 0.05, 0.1, 0.075])
    axbox_b = plt.axes([0.3, 0.05, 0.1, 0.075])
    axbox_c = plt.axes([0.5, 0.05, 0.1, 0.075])
    
    text_box_a = TextBox(axbox_a, 'a', initial=str(a))
    text_box_b = TextBox(axbox_b, 'b', initial=str(b))
    text_box_c = TextBox(axbox_c, 'c', initial=str(c))
    
    def submit(expression):
        try:
            a = float(text_box_a.text)
            b = float(text_box_b.text)
            c = float(text_box_c.text)
            y = a * x**2 + b * x + c
            l.set_ydata(y)
            ax.relim()
            ax.autoscale_view()
            plt.draw()
        except ValueError:
            pass

    text_box_a.on_submit(submit)
    text_box_b.on_submit(submit)
    text_box_c.on_submit(submit)
    
    plt.show()

# Coeficientes de la ecuación cuadrática inicial
a = 1
b = -3
c = 2

grafica_ecuacion_cuadratica(a, b, c)
