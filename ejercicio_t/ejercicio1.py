import matplotlib.pyplot as plt
import numpy as np

def euler(f, xi, yi, h, N):
    u = []
    v = []
    for i in range(N):
        yi = yi + h * f(xi, yi)
        xi = xi + h
        u.append(xi)
        v.append(yi)
    return u, v

def f(x, y):
    return 2*x*(1-y*np.exp(x*2))/(np.exp(x*2))

def exact_solution(x):
    return (x*2)/np.exp(x*2)

# Región R
x_min = 0
x_max = 1.5
y_min = 0
y_max = 1.5

# CI
xi = 0
yi = 0
h = 0.075
N = 20

u, v = euler(f, xi, yi, h, N)

# Calcular la solución exacta en el mismo intervalo
x_exact = np.linspace(xi, xi + N * h, 100)
y_exact = exact_solution(x_exact)

# Calcular el error en cada paso
errors = [abs(exact_solution(x) - y_approx) for x, y_approx in zip(u, v)]

# DIBUJAR SOLUCIÓN APROXIMADA
plt.plot(u, v, label='Solución aproximada (Euler)')

# DIBUJAR SOLUCIÓN EXACTA
plt.plot(x_exact, y_exact, label='Solución exacta', linestyle='--')

# DIBUJAR REGIÓN
plt.axvline(x=x_min, color='pink', label='Límite inferior de x')
plt.axvline(x=x_max, color='pink', label='Límite superior de x')
plt.axhline(y=y_min, color='green', label='Límite inferior de y')
plt.axhline(y=y_max, color='green', label='Límite superior de y')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Comparación entre Solución Exacta y Método de Euler')
plt.grid(True)
plt.show()

# Imprimir el valor de w_100 y el error
print(f"El valor aproximado de w_100 es {v[-1]}")
print(f"El valor exacto de y_100 es {exact_solution(x_exact[-1])}")
print(f"El error en el paso final es {errors[-1]}")