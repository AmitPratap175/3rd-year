import numpy as np
from math import *
import matplotlib.pyplot as plt
y0=0.5
def f(y,x):
    return -0.6*y+10*exp(-(x-2)**2/(2*(0.075)**2))

"""def rk4(tf,ti,h):
    n=ceil((tf-ti)/h)
    t= np.linspace(ti,tf,n+1)
    y0=0.5

    #rk 4
    y=[y0]
    for i in range(n):
        p=f(y[i],t[i])
        q=f(y[i]+(h/2)*p,t[i]+(h/2))
        r=f(y[i]+(h/2)*q,t[i]+(h/2))
        s=f(y[i]+h*r,t[i]+h)
        y.append(y[i]+(h/6)*(p+2*q+2*r+s))
    plt.plot(t,y)
    plt.legend( ["RK-4"])
    plt.xlabel('t')
    plt.ylabel('y')
"""   
    

def rk4_2(ti,h,yi,n):
    t=[ti]
    #rk 4
    y=[yi]
    for i in range(n):
        p=f(y[i],t[i])
        q=f(y[i]+(h/2)*p,t[i]+(h/2))
        r=f(y[i]+(h/2)*q,t[i]+(h/2))
        s=f(y[i]+h*r,t[i]+h)
        y.append(y[i]+(h/6)*(p+2*q+2*r+s))
        t.append(t[i]+h)
    return y,t,n

ti=0.
tf=4.
h=0.5
eps=0.00005
t=ti
tks=[ti]
tks_2=[ti]
y=[y0]
y_2=[y0]
while t<tf:
    y1,t1,n1=rk4_2(t,h,y[-1],1)
    y2,t2,n2=rk4_2(t,h/2,y[-1],2)
    delta=y2[-1]-y1[-1]
    if delta>eps:
            eta=0.25
    else:
            eta=0.2
    if(abs(delta)>eps):
        R=0.9
        h=R*h*(eps/abs(delta))**(eta)
    else:
        tks.append(t+h)
        """tks_2.append(t+h/2)
        tks_2.append(t+h)"""
        y.append(y1[-1])
        """y_2.append(y2[1])
        y_2.append(y2[2])"""
        t=t+h
    print(h)
#rk4(tf,ti,0.5)

plt.plot(tks,y)
plt.legend(['Rk4 adaptive'])
plt.xlabel('t')
plt.ylabel('y')
plt.show()
