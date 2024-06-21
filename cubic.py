import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def grafica_ecuacion_cubica(a, b, c, d):
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.35)
    x = np.linspace(-10, 10, 400)
    y = a * x**3 + b * x**2 + c * x + d
    l, = plt.plot(x, y, lw=2)
    plt.title('Gráfica de la Ecuación de Tercer Grado')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    
    # Definir la posición de las cajas de texto
    axbox_a = plt.axes([0.1, 0.05, 0.1, 0.075])
    axbox_b = plt.axes([0.25, 0.05, 0.1, 0.075])
    axbox_c = plt.axes([0.4, 0.05, 0.1, 0.075])
    axbox_d = plt.axes([0.55, 0.05, 0.1, 0.075])
    
    text_box_a = TextBox(axbox_a, 'a', initial=str(a))
    text_box_b = TextBox(axbox_b, 'b', initial=str(b))
    text_box_c = TextBox(axbox_c, 'c', initial=str(c))
    text_box_d = TextBox(axbox_d, 'd', initial=str(d))
    
    def submit(expression):
        try:
            a = float(text_box_a.text)
            b = float(text_box_b.text)
            c = float(text_box_c.text)
            d = float(text_box_d.text)
            y = a * x**3 + b * x**2 + c * x + d
            l.set_ydata(y)
            ax.relim()
            ax.autoscale_view()
            plt.draw()
        except ValueError:
            pass

    text_box_a.on_submit(submit)
    text_box_b.on_submit(submit)
    text_box_c.on_submit(submit)
    text_box_d.on_submit(submit)
    
    plt.show()

# Coeficientes de la ecuación de tercer grado inicial
a = 1
b = -3
c = 2
d = 0

grafica_ecuacion_cubica(a, b, c, d)
