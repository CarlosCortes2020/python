import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def grafica_linea_recta(m, b):
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    x = np.linspace(-10, 10, 400)
    y = m * x + b
    l, = plt.plot(x, y, lw=2)
    plt.title('Gráfica de la Línea Recta')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    
    # Definir la posición de las cajas de texto
    axbox_m = plt.axes([0.1, 0.05, 0.1, 0.075])
    axbox_b = plt.axes([0.3, 0.05, 0.1, 0.075])
    
    text_box_m = TextBox(axbox_m, 'm', initial=str(m))
    text_box_b = TextBox(axbox_b, 'b', initial=str(b))
    
    def submit(expression):
        try:
            m = float(text_box_m.text)
            b = float(text_box_b.text)
            y = m * x + b
            l.set_ydata(y)
            ax.relim()
            ax.autoscale_view()
            plt.draw()
        except ValueError:
            pass

    text_box_m.on_submit(submit)
    text_box_b.on_submit(submit)
    
    plt.show()

# Valores iniciales de la pendiente y la intersección
m = 1
b = 0

grafica_linea_recta(m, b)
