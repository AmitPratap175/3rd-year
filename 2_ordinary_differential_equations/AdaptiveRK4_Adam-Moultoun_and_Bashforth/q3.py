import numpy as np
from math import *
import matplotlib.pyplot as plt

def f(y,t):
    return -2*y/(1+t)
def g(x):
    return 2/(1+x)**2



def adam(h):
    t=np.linspace(ti,tf,ceil((tf-ti)/h)+1)
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0, 3):
        p = f(y[n], t[n])
        q= f(y[n] + h*p/2, t[n] + h/2)
        r= f(y[n] + h*q/2, t[n] + h/2)
        s = f(y[n] + h*r, t[n] + h)
        y[n+1] = y[n] + (h/6)*(p+ 2*q+ 2*r + s)
    for n in range(3, len(t)-1):
        y[n+1]=y[n]+h*(np.dot(adam_b,f(y[n-3:n+1:1],t[n-3:n+1:1])))
        y[n+1]=y[n]+h*(np.dot(adam_m,f(y[n-2:n+2:1],t[n-2:n+2:1])))
    return y,t,ceil((tf-ti)/h)
   
ti=0
tf=2.5
y0=2.
adam_b=[-3/8,37/24,-59/24,55/24]
adam_m=[1/24,-5/24,19/24,3/8]

h=[0.05, 0.02]
y1,t1,n1=adam(h[0])
y2,t2,n2=adam(h[1])

plt.plot(t1,y1)
plt.plot(t2,y2)
t=np.linspace(ti,tf,1000)
plt.plot(t,g(t),'r--')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['h=0.05','h=0.02','Actual'])
plt.show()

plt.plot(t1,g(t1)-y1)
plt.plot(t2,g(t2)-y2)
print(np.amax(g(t1)-y1))
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['h=0.05 error','h=0.02 error'])
plt.show()
err=[]
x=[]
for i in range(n1+1):
    for j in range(n2+1):
        if(t1[i]==t2[j]):
            err.append(abs(y1[i]-y2[j]))
            x.append(t1[i])
plt.plot(x,err)
plt.xlabel('t')
plt.ylabel('error ')
plt.show()
