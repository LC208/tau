import matplotlib.pyplot as pyplot

import matplotlib as matplotlib
import numpy as numpy

T1 = 0.1
T2 = 0.02
k = 0.1
g = 1

def f1(y, z2):
    return z2 - (T1/(T2*T2))*y

def f2(y):
    return (k/(T2*T2))*g -(1/(T2*T2))*y

y=0
z2=0
dt = T2/100
L = 4*T1
t = 0
X = list()
W = list()
H = list()
one = list()
w = 0
while t < L:
    X.append(t)
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
    if t > 0:
        w = (H[len(H)-1] - y)/dt
    t+=dt
pyplot.plot(X, H, color="orange", label = "Переходная функция")
pyplot.plot(X, W, color="blue", label="Весовая функция")
pyplot.plot(X, one, label = "Единичное ступенчатое воздействие")
pyplot.grid(True)
pyplot.legend()
pyplot.show()