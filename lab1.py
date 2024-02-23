import matplotlib.pyplot as pyplot

import matplotlib as matplotlib
import numpy as numpy

k = 0.1
T1 = 0.1
T2=0.02
g = 1

def f1(z):
    return z

def f2(u,z):
    return -(T1/(T2*T2))*z - 1/(T2*T2)*u+g

y=0
u=0
z=0
dt = T2/10
L = 3*T1
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
    k1 = dt*f1(z)
    q1 = dt*f2(u,z)
    k2 = dt*f1(z+q1/2)
    q2 = dt*f2(u+k1/2,z+q1/2)
    k3 = dt*f1(z+q2/2)
    q3 = dt*f2(u+k2/2,z+q2/2)
    k4 = dt*f1(z+q3)
    q4 = dt*f2(u+k3,z+q3)
    z = z + (q1+2*q2+2*q3+q4)/6
    u = u + (k1+2*k2+2*k3+k4)/6
    y = (k*u)/(T2*T2)
    if t > 0:
        w = (H[len(H)-1] - y)/dt
    t+=dt
pyplot.plot(X, H, color="orange", label = "Переходная функция")
pyplot.plot(X, W, color="blue", label="Весовая функция")
pyplot.plot(X, one, label = "Единичное ступенчатое воздействие")
pyplot.grid(True)
pyplot.legend()
pyplot.show()