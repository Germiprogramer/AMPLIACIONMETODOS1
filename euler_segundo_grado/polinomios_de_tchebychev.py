#esta bien

import numpy as np
import matplotlib.pyplot as plt

def rungekutta(f, a, b, u0, v0, n):
    
    h = (b-a)/N
    x = a
    u = u0
    v = v0
    u_valores = [u0]
    x_valores = [x]
    for i in range(n+1):
        k11 = v
        k12 = f(x,u,v)
        k21 = v + h*k12/2
        k22 = f(x+h/2,u+h*k11/2,v+h*k12/2)
        k31 = v + h*k22/2
        k32 = f(x+h/2,u+h*k21/2,v+h*k22/2)
        k41 = v + h*k32
        k42 = f(x+h,u+h*k31,v+h*k32)
        u = u + h*(k11+2*k21+2*k31+k41)/6
        v = v + h*(k12+2*k22+2*k32+k42)/6
        x = a + i*h

        u_valores.append(u)
        x_valores.append(x)
    return x, u, x_valores, u_valores


#t es el termino independiente
t = 0
n=1
u0 = (-1)**n
v0 = n/2
a = -1
b = 0.99
N = 10000

#despejando y'' = f(x,y,y')
#corregir esto en funcion de p y q

def f(x, u, v, n):
    return ((x*v - (n**2)*u)/(1-x**2))

x, u, x_valores, u_valores = rungekutta(f, a, b, u0, v0, N)
print("u: " + str(u))
print("x: " + str(x))

plt.plot(x_valores, u_valores)
plt.show()