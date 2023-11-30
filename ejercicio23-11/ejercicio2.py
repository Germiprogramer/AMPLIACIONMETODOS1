#codigo perfecto

import matplotlib.pyplot as plt
import numpy as np

# Ecuacion 1
def edo1(x, y):
    return 2*x*(np.exp(-x**2) - y)

def solucion_exacta(x, c):
    return (x**2 + c)*np.exp(-x**2)

def Euler(a, b, y0, f, n):
    h = (b - a)/n
    x = a
    y = y0
    x_aprox = [x]
    y_aprox = [y]
    for i in range(0, n):
        y = y + h*f(x, y)
        x = a + i*h
        y_aprox.append(y)
        x_aprox.append(x)
    return x_aprox, y_aprox

extremo_inf = 0
extremo_sup = 2
N = 100

# Condiciones iniciales para y
y0_range = [0, 1, -1]
c_values = [0, 1, -1]

# Gráfica de las soluciones
for i in range(len(y0_range)):
    y0 = y0_range[i]
    c = c_values[i]
    
    # Solución numérica con el método de Euler
    x_num, y_num = Euler(extremo_inf, extremo_sup, y0, edo1, N)
    plt.plot(x_num, y_num, label="Aproximada con y0 = " + str(y0))

    # Solución exacta
    x_exacta = np.linspace(extremo_inf, extremo_sup, 100)
    y_exacta = solucion_exacta(x_exacta, c)
    plt.plot(x_exacta, y_exacta, label="Exacta con y0 = " + str(y0) + " y c = " + str(c), linestyle='--')

plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title("Soluciones de la EDO1 con el Método de Euler")
plt.legend()
plt.grid(True)
plt.show()
