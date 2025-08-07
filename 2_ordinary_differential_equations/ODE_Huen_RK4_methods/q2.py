import numpy as np
from math import *
import matplotlib.pyplot as plt


ti=0.
tf=3.
def f(y,t):
    return (-2*y+t**2)
def g(x):
    return (2*x**2-2*x+1+3*np.exp(-2*x))/4
y0=1.
h=0.1
n=ceil((tf-ti)/h)
t= np.linspace(ti,tf,n+1)

y=[y0]
for i in range(n):
    p=f(y[i],t[i])
    q=f(y[i]+(h/2)*p,t[i]+(h/2))
    r=f(y[i]+2*q*h-p*h,t[i]+h)
    y.append(y[i]+(h/6)*(p+4*q+r))
print(y)
plt.plot(t,y)
#plt.plot(t,g(t))
plt.legend(["RK-3"])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.plot(t,np.abs(y-g(t)))
plt.legend(["Error"])
plt.xlabel('x')
plt.ylabel('Error')
plt.show()
