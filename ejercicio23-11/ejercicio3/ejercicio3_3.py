import matplotlib.pyplot as plt
import numpy as np

'Ecuacion 1'
# Define la función f(x, y) para la EDO
def edo1(x, y):
    return 2*x*(np.exp(-x**2) - y)

def solucion_exacta(x):
    return (x**2)*np.exp(-x**2)

#Funcion para el metodo de euler
def Runge_kutta(a, b, y0, f, n):
    h = (b - a)/n
    x = a
    y = y0
    x_aprox = [x]
    y_aprox = [y]
    for i in range(0, n+1):
        y = y + h*f(x+(h/2), y+h*f(x, y)/2)
        x = a + i*h
        y_aprox.append(y)
        x_aprox.append(x)
    return x, y

#Pedimos por pantalla los extremos del intervalo
extremo_inf = float(input("Ingrese el extremo inferior del intervalo: "))
extremo_sup = float(input("Ingrese el extremo superior del intervalo: "))
N = 5 #Asumimos un numero de 100 intervalos

#Condiciones iniciales de la primera edo
y0_range = [0]  # Condiciones iniciales para y
x0_range = [0]  # Condiciones iniciales para x
#Con este bucle mostramos la grafica
for i in range(len(y0_range)):
    y0 = y0_range[i]
    x0 = x0_range[i]
    x_euler, y_euler = Runge_kutta(extremo_inf, extremo_sup, y0, edo1, N)

print("y_euler: " + str(y_euler))
print("x_euler: " + str(x_euler))
print("y exacto: " + str(solucion_exacta(extremo_sup)))
error = abs(solucion_exacta(extremo_sup) - y_euler)
print("Error absoluto para y0 = " + str(y0) + ": " + str(error))