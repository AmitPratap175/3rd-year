import numpy as np
from math import *
import matplotlib.pyplot as plt

h=[0.0005, 0.0015]
ti=0.
tf=0.006
y0=0.

def f(t,y):
    return -1000*y+3000-2000*exp(-t)
def g(t):
    return 3-0.998*np.exp(-1000*t)-2.002*np.exp(-t)

for i in range(2):
    n=ceil((tf-ti)/h[i])
    t=np.linspace(ti,tf,n+1)
    y=[y0]
    for j in range(n):
        y.append(y[j]+h[i]*f(t[j],y[j]))
    plt.plot(t,y)
t=np.linspace(ti,tf,100000)
plt.plot(t,g(t))
plt.legend(['h=0.0005','h=0.0015','Actual analytical solution'])
plt.xlabel('t')
plt.ylabel('y')
plt.show()
