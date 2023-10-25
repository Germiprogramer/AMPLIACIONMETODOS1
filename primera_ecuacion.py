import matplotlib.pyplot as plt

# Definir la función f(x, y)
def f(x, y):
    return (2 - x - y) / (x - y + 4)  # Puedes cambiar esta función según tus necesidades

# Condiciones iniciales
x0_1 = -2
y0_1 = 0
x0_2 = 0
y0_2 = 5.6
x0_3 = 2.71828  # Valor aproximado de e
y0_3 = 6

# Tamaño del paso
h = 0.1

# Número de iteraciones
num_iteraciones = 300

# Listas para almacenar los valores de x e y
x_vals_1 = [x0_1]
y_vals_1 = [y0_1]
x_vals_2 = [x0_2]
y_vals_2 = [y0_2]
x_vals_3 = [x0_3]
y_vals_3 = [y0_3]

# Calcular las sucesiones usando bucles
for i in range(num_iteraciones):
    x_next_1 = x_vals_1[-1] + h
    y_next_1 = y_vals_1[-1] + h * f(x_vals_1[-1], y_vals_1[-1])
    x_vals_1.append(x_next_1)
    y_vals_1.append(y_next_1)

    x_next_2 = x_vals_2[-1] - h
    y_next_2 = y_vals_2[-1] - h * f(x_vals_2[-1], y_vals_2[-1])
    x_vals_2.append(x_next_2)
    y_vals_2.append(y_next_2)

    x_next_3 = x_vals_3[-1] + h
    y_next_3 = y_vals_3[-1] + h * f(x_vals_3[-1], y_vals_3[-1])
    x_vals_3.append(x_next_3)
    y_vals_3.append(y_next_3)

# Graficar los puntos resultantes
plt.figure(figsize=(8, 6))
plt.axis([-20, 20, -20, 20])
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.plot(x_vals_1, y_vals_1, marker='o', linestyle='-', color='r', linewidth=0.5, label='Sucesión 1')
plt.plot(x_vals_2, y_vals_2, marker='o', linestyle='-', color='b', linewidth=0.5, label='Sucesión 2')
plt.plot(x_vals_3, y_vals_3, marker='o', linestyle='-', color='g', linewidth=0.5, label='Sucesión 3')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sucesiones')
plt.legend()
plt.grid(True)
plt.show()

