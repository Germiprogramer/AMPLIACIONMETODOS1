import numpy as np
import matplotlib.pyplot as plt

def euler_segundo_orden(f, a, b, u0, v0, t, n, p, q):
    
    h = (b-a)/N
    x = a
    u = u0
    v = v0
    u_valores = [u0]
    x_valores = [x]
    for i in range(n+1):
        w = u
        u = u + h*v
        v = v + h*(-q(x,0)*w - p(x)*v+t)
        x = a + i*h
        u_valores.append(u)
        x_valores.append(x)
    return x, u, x_valores, u_valores

def p(x):
    return -(2*x)/((1-x**2))

def q(x, n):
    return (n*(n+1)/(1-x**2))

#t es el termino independiente
t = 0
u0 = 1
v0 = 0
a = 0.1
b = 1
N = 10000

def f(x, u, v):
    return 1-v-u

x, u, x_valores, u_valores = euler_segundo_orden(f, a, b, u0, v0, t, N, p, q)
print("u: " + str(u))
print("x: " + str(x))

plt.plot(x_valores, u_valores)
plt.show()