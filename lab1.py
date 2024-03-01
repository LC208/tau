import matplotlib.pyplot as pyplot

import matplotlib as matplotlib
from numpy import sin,exp,sqrt,cos, pi

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
L = (6*pi*T)/sqrt(1+eps*eps)
t = 0
X = list()
W = list()
HA = list()
WO= list()
HO= list()
WA = list()
H = list()
one = list()
a = 1/50
b = sqrt(6)/25
w = 0
while t < L:
    X.append(t)
    HA.append(k+exp(-a*t)*(k*(-a/b)*sin(b*t)-k*cos(b*t)))
    HO.append(k-(k*sin(b*t)+2*sqrt(6)*k*cos(b*t))/(2*sqrt(6)*exp(a*t)))
    WO.append((k*exp(-a*t)*sin(b*t))/(4*sqrt(6)))
    WA.append(k*exp(-a*t)*sin(b*t)*(b+((a*a)/b)))
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
pyplot.plot(X, H, color="blue", linewidth = 6, label = "Переходная функция")
pyplot.plot(X, W, color="blue", linewidth = 6,label="Весовая функция")
pyplot.plot(X, one, label = "Единичное ступенчатое воздействие", color = "green")
pyplot.plot(X,HA, label = "Аналитически расчитанная переходная функция", linestyle="dashed", color = "black", linewidth = 4)
pyplot.plot(X,WA, label = "Аналитически расчитанная весовая функция",linestyle="dashed", color = "black", linewidth = 4)
pyplot.plot(X,WO, label = "Операторная весовая функция", linestyle="dashed", color = "red")
pyplot.plot(X,HO, label = "Операторная переходная функция", linestyle="dashed", color = "red")
pyplot.grid(True)
# pyplot.legend()
pyplot.show()