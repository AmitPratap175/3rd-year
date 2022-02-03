import numpy as np
from math import *
import matplotlib.pyplot as plt

def f(y,t):
    return (1+4*t)*sqrt(y)
def g(x):
    return (2*x**2+x+2)**2/4

ti=float(input("Enter the initial t value:  "))
tf=float(input("Enter the final t value:  "))
h=float(input("Enter the step size:  "))
n=ceil((tf-ti)/h)
t= np.linspace(ti,tf,n+1)
y0=float(input("Enter the initial value of y:  "))

#Euler
y=[y0]
for i in range(n):
    y.append(y[i]+h*f(y[i],t[i]))
print(y)
    
#huens method
y1=[y0]
for i in range(n):
    y_=y1[i]+h*f(y1[i],t[i])
    y1.append(y1[i]+(h/2)*(f(y1[i],t[i])+f(y_,t[i+1])))
print(y1)

#ralston
y2=[y0]
alpha=2/3
b1=1/4
b2=3/4
for i in range(n):
    p=f(y2[i],t[i])
    q=f(y2[i]+alpha*h*p,t[i]+alpha*h)
    y2.append(y2[i]+h*(b1*p+b2*q))
print(y2)

#rk 4
y3=[y0]
for i in range(n):
    p=f(y3[i],t[i])
    q=f(y3[i]+(h/2)*p,t[i]+(h/2))
    r=f(y3[i]+(h/2)*q,t[i]+(h/2))
    s=f(y3[i]+h*r,t[i]+h)
    y3.append(y3[i]+(h/6)*(p+2*q+2*r+s))
print(y3)

plt.plot(t,g(t))
plt.plot(t,y)
plt.plot(t,y1)
plt.plot(t,y2)
plt.plot(t,y3)
plt.legend(["Actual", "Euler's method","Huen's method","Ralston's method","RK-4"])
plt.show()
