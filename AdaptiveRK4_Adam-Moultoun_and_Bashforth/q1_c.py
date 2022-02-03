import numpy as np
from math import *
import matplotlib.pyplot as plt

h=0.05
ti=0.05
tf=0.4
y0=0.

def f(t,y):
    return -1000*y+3000-2000*exp(-t)
def g(t):
    return 3-0.998*np.exp(-1000*t)-2.002*np.exp(-t)
print(g(0.05))

n=ceil((tf-ti)/h)
t=np.linspace(ti,tf,n+1)
yi=(y0+h*(3000-2000*exp(-0.05)))/(1+1000*h)
print(yi)
y=[yi]
for j in range(n):
    y.append((y[j]+h*(3000-2000*exp(-t[j+1])))/(1+1000*h))
plt.plot(t,y)
x=np.linspace(ti,tf,100000)
plt.plot(x,g(x))
plt.legend(['h=0.05','Actual analytical solution'])
plt.xlabel('t')
plt.ylabel('y')
plt.show()

