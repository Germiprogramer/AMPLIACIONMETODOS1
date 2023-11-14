import matplotlib.pyplot as plt
import numpy as np

'Ecuacion 1'
# Define la función f(x, y) para la EDO
def edo1(x, y):
    return (2-x-y)/(x-y+4)

#Funcion para el metodo de euler
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

#Pedimos por pantalla los extremos del intervalo
extremo_inf = float(input("Ingrese el extremo inferior del intervalo: "))
extremo_sup = float(input("Ingrese el extremo superior del intervalo: "))
N = 100 #Asumimos un numero de 100 intervalos

#Condiciones iniciales de la primera edo
y0_range = [0, 4, 4.33]  # Condiciones iniciales para y
x0_range = [-2, -2, 2]  # Condiciones iniciales para x

#Con este bucle mostramos la grafica
for i in range(len(y0_range)):
    y0 = y0_range[i]
    x0 = x0_range[i]
    x, y = Euler(x0, extremo_sup, y0, edo1, N)
    plt.plot(x, y, label="Solución Aproximada con y0 = " + str(y0))

plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=1) #Eje x
plt.axvline(0, color='black', linewidth=1) #Eje y
plt.title("Solución de la EDO1 con el Método de Euler")
plt.legend()
plt.grid(True)
plt.show()

#Hay que cerrar la imagen para que se siga ejecutando el codigo



'Ecuacion 2'
# Definimos la función f(x, y) para la segunda EDO
def edo2(x, y):
    return 2*x*np.exp(-3*x) - 3*y

#Volvemos a pedir por pantalla los extremos
extremo_inf = float(input("Ingrese el extremo inferior del intervalo: "))
extremo_sup = float(input("Ingrese el extremo superior del intervalo: "))

#Condiciones iniciales de la primera edo
y0_range = [2, 2]  # Condiciones iniciales para y
x0_range = [-0.8, -0.2]  # Condiciones iniciales para x

#Con este bucle  y las instrucciones siguientes mostramos la grafica
for i in range(len(y0_range)):
    y0 = y0_range[i]
    x0 = x0_range[i]
    x, y = Euler(x0, extremo_sup, y0, edo2, N)
    plt.plot(x, y, label="Solución Aproximada con y0 = " + str(y0))

plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=1) #Eje x
plt.axvline(0, color='black', linewidth=1) #Eje y
plt.title("Solución de la EDO2 con el Método de Euler")
plt.legend()
plt.grid(True)
plt.show()