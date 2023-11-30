import matplotlib.pyplot as plt
import numpy as np

'Ecuacion 1'
# Define la función f(x, y) para la EDO
def edo1(x, y):
    return y - x**2 + 1

def solucion_exacta(x):
    return (x+1)**2 + (0.5)*np.exp(x)

#Funcion para el metodo de euler
def Runge_kutta_2(a, b, y0, f, n):
    h = (b - a)/n
    x = a
    y = y0
    x_aprox = [x]
    y_aprox = [y]
    for i in range(0, n):
        k_1 = f(x, y)
        k_2 = f(x+(h/2), y+(h/2)*k_1)
        k_3 = f(x+(h/2), y+(h/2)*k_2)
        k_4 = f(x+h, y+h*k_3)
        y = y + h*((1/6)*k_1+(1/3)*k_2+(1/3)*k_3+(1/6)*k_4)
        x = a + i*h
        y_aprox.append(y)
        x_aprox.append(x)
    return x_aprox, y_aprox

def error_absoluto(solucion_exacta, x_numerico, y_numerico):
    # Calcula el valor de la solución exacta en los puntos numéricos
    y_exacto = [solucion_exacta(xi) for xi in x_numerico]
    print("y_exacto: " + str(y_exacto))

    # Calcula el error absoluto en cada punto
    error_abs = [abs(yn - ye) for yn, ye in zip(y_numerico, y_exacto)]
    
    print("y_numerico: " + str(y_numerico))
    

    return error_abs

#Pedimos por pantalla los extremos del intervalo
extremo_inf = float(input("Ingrese el extremo inferior del intervalo: "))
extremo_sup = float(input("Ingrese el extremo superior del intervalo: "))
N = 5 #Asumimos un numero de 100 intervalos

#Condiciones iniciales de la primera edo
y0_range = [0.5]  # Condiciones iniciales para y
x0_range = [0]  # Condiciones iniciales para x
#Con este bucle mostramos la grafica
for i in range(len(y0_range)):
    y0 = y0_range[i]
    x0 = x0_range[i]
    x, y = Runge_kutta_2(x0, extremo_sup, y0, edo1, N)
    plt.plot(x, y, label="Solución Aproximada con y0 = " + str(y0))
error = error_absoluto(solucion_exacta, x, y)
print("Error absoluto para y0 = " + str(y0) + ": " + str(error[-1]))

plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=1) #Eje x
plt.axvline(0, color='black', linewidth=1) #Eje y
plt.title("Solución de la EDO1 con el Método de Euler")
plt.legend()
plt.grid(True)
plt.show()