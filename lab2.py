import matplotlib.pyplot as pyplot

import matplotlib as matplotlib
from numpy import sin,exp,sqrt,cos, pi

T = 10
eps = 0.1
k = 1
g = 1

def f1(y, z2):
    return z2-(2*eps*y)/T

def f2(y):
    return (k/(T*T))*g - (1/(T*T))*y

def r_k(w, y, z2, f1, f2,W,H):
    W.append(w)
    H.append(y)
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
    return y,w,z2



X = list()
W = list()
H = list()
W1 = list()
H1 = list()
one = list()
y=0
z2=0
w = 0
y1=0
w1=0
z21=0
dt = T/100
L = (6*pi*T)/sqrt(1+eps*eps)
t = 0
koc = 2 #4
while t < L:
    X.append(t)
    one.append(1)
    y1,w1,z21 =r_k(w1,y1,z21,f1,f2,W1,H1)
    g = 1
    y,w,z2 =r_k(w,y,z2,f1,f2,W,H)
    g = 1 - W1[len(W) - 1]*koc
    t+=dt
pyplot.plot(X, H, color="blue", linewidth = 1, label = "Смоделированная переходная функция")
pyplot.plot(X, H1, color="red", linewidth = 1, label = "Смоделированная переходная функция с ПОС")
#pyplot.plot(X, one, label = "Единичное ступенчатое воздействие", color = "green")
pyplot.grid(True)
pyplot.legend()
pyplot.show()