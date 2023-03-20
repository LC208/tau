import matplotlib.pyplot as pyplot

import matplotlib as matplotlib
from numpy import sin,exp,sqrt,cos, pi

T1 = 0.1
C3 = 8 
C2 = sqrt(C3)
T2 = C2*T1
T3 = C3*T1
k= 2 + (C2+C2*C2+C2*C2*C3+C3*C3*C2+C3+C3*C3)/(C2*C3)
k=15
def f1(y, x):
    return (k*x/T1)-(y/T1)

def f2(y,x):
    return (x/T2)-(y/T2)
def f3(y,x):
    return (x/T3)-(y/T3)

def r_k(y, f, x):
    k1 = dt*f(y,x)
    k2 = dt*f(y+k1/2,x)
    k3 = dt*f(y+k2/2,x)
    k4 = dt*f(y+k3,x)
    yn = y + (k1+2*k2+2*k3+k4)/6
    return yn

X = list()
H = list()
y1=0
y2=0
y3=0
dt = 1/1000
L = 20
t = 0
x = 1
while t < L:
    X.append(t)
    H.append(y3)
    x = 1 - y3
    y1 =r_k(y1,f1,x)
    y2 =r_k(y2,f2,y1)
    y3 =r_k(y3,f3,y2)
    t+=dt
pyplot.plot(X, H, color="blue", linewidth = 1, label = "Смоделированная переходная функция")
pyplot.grid(True)
pyplot.legend()
pyplot.show()