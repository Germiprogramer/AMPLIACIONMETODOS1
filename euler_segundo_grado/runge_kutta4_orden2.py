#no esta bien

import numpy as np

p=3
q=1
r=2
s=1
x0=10
y0=5
N=1000

def FuncionX(x,u,v):
    return p*u-q*u*v

def FuncionY(x,u,v):
    return -r*u+s*v+1

a = float(input("Extremo inferior: "))
b = float(input("Extremo superior: "))
h = (b-a)/N

x = np.zeros(N+1)
y1 = np.zeros(N+1)
y2 = np.zeros(N+1)

x[0] = a
y1[0] = float(input("Ingrese el valor de y1: ")) #10
y2[0] = float(input("Ingrese el valor de y2: ")) #5

for k in range (N):
    k11=FuncionX(x[k],y1[k],y2[k])
    k12=FuncionY(x[k],y1[k],y2[k])
    k21=FuncionX(x[k]+h/2,y1[k]+h*k11/2,y2[k]+h*k12/2)
    k22=FuncionY(x[k]+h/2,y1[k]+h*k11/2,y2[k]+h*k12/2)
    k31=FuncionX(x[k]+h/2,y1[k]+h*k21/2,y2[k]+h*k22/2)
    k32=FuncionY(x[k]+h/2,y1[k]+h*k21/2,y2[k]+h*k22/2)
    k41=FuncionX(x[k]+h,y1[k]+h*k31,y2[k]+h*k32)
    k42=FuncionY(x[k]+h,y1[k]+h*k31,y2[k]+h*k32)
    x[k+1]=x[k]+h
    y1[k+1]=y1[k]+h*(k11+2*k21+2*k31+k41)/6
    y2[k+1]=y2[k]+h*(k12+2*k22+2*k32+k42)/6

#graficame todo
import matplotlib.pyplot as plt
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
