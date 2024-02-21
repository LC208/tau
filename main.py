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
    return (k/(T*T))*g - (1/T*T)*y

y=0
z2=0
dt = T/100
L = (6*numpy.pi*T)/numpy.sqrt(1+eps*eps)
t = 0
X = list()
W = list()
H = list()
one = list()
ypr = 0
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
    ypr = y
    y = y + (k1+2*k2+2*k3+k4)/6
    if t > 0:
        w = (ypr - y)/dt
    t+=dt
#pyplot.bar(X, H, label = "Переходная функция",alpha = 0.5)
#pyplot.bar(X, W, label="Весовая функция", alpha = 0.5)
#pyplot.bar(X, one, label = "Единичное ступенчатое воздействие", alpha = 0.5)
pyplot.plot(X, H, color="orange")
pyplot.plot(X, W, color="blue")
pyplot.plot(X, one)
pyplot.show()