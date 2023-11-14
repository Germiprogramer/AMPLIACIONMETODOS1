import matplotlib.pyplot as plt
import numpy as np

# Definir la función f(x, y)
def f(x, y):
    return 2 * x * np.exp(-3 * x) - 3 * y

# Condiciones iniciales
x0_1 = -0.7
y0_1 = 0
x0_2 = 0
y0_2 = 1

# Tamaño del paso
h = 0.1

# Número de iteraciones
num_iteraciones = 300

# Listas para almacenar los valores de x e y
x_vals_1 = [x0_1]
y_vals_1 = [y0_1]
x_vals_2 = [x0_2]
y_vals_2 = [y0_2]

# Calcular las sucesiones usando bucles
for i in range(num_iteraciones):
    x_next_1 = x_vals_1[-1] + h
    y_next_1 = y_vals_1[-1] + h * f(x_vals_1[-1], y_vals_1[-1])
    x_vals_1.append(x_next_1)
    y_vals_1.append(y_next_1)

    x_next_2 = x_vals_2[-1] + h
    y_next_2 = y_vals_2[-1] + h * f(x_vals_2[-1], y_vals_2[-1])
    x_vals_2.append(x_next_2)
    y_vals_2.append(y_next_2)

# Graficar los puntos resultantes
plt.figure(figsize=(8, 6))
plt.axis([-2, 2, -2, 2])
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.plot(x_vals_1, y_vals_1, marker='o', linestyle='-', color='r', linewidth=0.5, label='Sucesión 1')
plt.plot(x_vals_2, y_vals_2, marker='o', linestyle='-', color='b', linewidth=0.5, label='Sucesión 2')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sucesiones para $f(x, y) = 2xe^{-3x} - 3y$')
plt.legend()
plt.grid(True)
plt.show()
