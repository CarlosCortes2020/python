import numpy as np
import matplotlib.pyplot as plt

def grafica_ecuacion_cuadratica(a, b, c):
    # Definimos el rango de valores para x
    x = np.linspace(-10, 10, 400)
    # Calculamos los valores correspondientes de y
    y = a * x**2 + b * x + c

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
    plt.title('Gráfica de la Ecuación Cuadrática')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

# Coeficientes de la ecuación cuadrática
a = 1
b = -3
c = 2

grafica_ecuacion_cuadratica(a, b, c)
