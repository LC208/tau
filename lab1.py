import matplotlib.pyplot as pyplot

import matplotlib as matplotlib
import numpy as numpy

T = 10
eps = 0.2
k = 1
g = 1

def f1(y, z2):
    return z2-(2*eps*y)/T

def f2(y):
    return (k/(T*T))*g - (1/(T*T))*y

y=0
z2=0
dt = T/100
L = (6*numpy.pi*T)/numpy.sqrt(1+eps*eps)
t = 0
X = list()
W = list()
HA = list()
WO= list()
WA = list()
H = list()
one = list()
a = 1/50
b = numpy.sqrt(6)/25
w = 0
while t < L:
    X.append(t)
    HA.append(k+numpy.exp(-a*t)*((-k*(a/b))*numpy.sin(b*t)-k*numpy.cos(b*t)))
    WO.append((k*numpy.exp(-a*t)*numpy.sin(b*t))/(4*numpy.sqrt(6)))
    WA.append((numpy.exp(-a*t)/(100*numpy.sqrt(6)))*((24*k-1)*numpy.sin(b*t)+ 2*numpy.sqrt(6)*(k+1)*numpy.cos(b*t)))
    W.append(w)
    H.append(y)
    one.append(1)
    k1 = dt*f1(y,z2)
    q1 = dt*f2(y)
    k2 = dt*f1(y+k1/2,z2+q1/2)
    q2 = dt*f2(y+k1/2)
    k3 = dt*f1(y+k2/2,z2+q2/2)
    q3 = dt*f2(y+k2/2)
    k4 = dt*f1(y+k3,z2+q3)
    q4 = dt*f2(y+k3)
    z2 = z2 + (q1+2*q2+2*q3+q4)/6
    y = y + (k1+2*k2+2*k3+k4)/6
    w = (y - H[len(H)-1])/dt
    t+=dt
pyplot.plot(X, H, color="orange", label = "Переходная функция")
pyplot.plot(X, W, color="blue", label="Весовая функция")
pyplot.plot(X, one, label = "Единичное ступенчатое воздействие")
pyplot.plot(X,HA, label = "Аналитически расчитанная переходная функция", linestyle="dashed", color = "black")
pyplot.plot(X,WO, label = "Операторная весовая функция", linestyle="dashed", color = "red")
pyplot.plot(X,WA, label = "Аналитически расчитанная весовая функция")
pyplot.grid(True)
pyplot.legend()
pyplot.show()