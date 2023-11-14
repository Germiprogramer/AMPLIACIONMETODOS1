import matplotlib.pyplot as plt

# Definir la ecuación diferencial dy/dx = (1 + 4xy) / x^2
def dy_dx(x, y):
    return (1 + 4 * x * y) / x**2

# Condiciones iniciales
x0 = 0.5
y0 = -3

# Tamaño del paso
h = 0.035

# Número de iteraciones
num_iteraciones = 100

# Listas para almacenar los valores de x e y
x_vals = [x0]
y_vals = [y0]

# Calcular la solución usando el método de Euler
for i in range(num_iteraciones):
    x_next = x_vals[-1] + h
    y_next = y_vals[-1] + h * dy_dx(x_vals[-1], y_vals[-1])
    
    # Aplicar cotas
    x_next = max(0.5, min(4, x_next))
    y_next = max(-3, min(3, y_next))
    
    x_vals.append(x_next)
    y_vals.append(y_next)

# Graficar la solución
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='b', linewidth=0.5, label='Solución')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Método de Euler para y\' = (1 + 4xy) / x^2')
plt.legend()
plt.grid(True)
plt.show()
print(x_vals[-1], y_vals[-1])
