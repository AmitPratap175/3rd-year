import numpy as np
from math import *
import matplotlib.pyplot as plt

def f(y,z,t):
    return -2*y+5*exp(-t)
def g(x):
    return (5*np.exp(x)-3)*np.exp(-2*x)

def f2(y,z,t):
    return -y*z**2/2
def g2(x):
    return 4*np.exp(2*x)/(8*exp(2*x)-10*np.exp(x)+3)
g2_=np.vectorize(g2)
ti=0.
tf=0.4
h=0.1
n=ceil((tf-ti)/h)
t= np.linspace(ti,tf,n+1)
y0=2.


#rk 4
y=[y0]
z0=4.
z=[z0]
for i in range(n):
    p1=f(y[i],z[i],t[i])
    p2=f2(y[i],z[i],t[i])
    q1=f(y[i]+(h/2)*p1,z[i]+(h/2)*p2,t[i]+(h/2))
    q2=f2(y[i]+(h/2)*p1,z[i]+(h/2)*p2,t[i]+(h/2))
    r1=f(y[i]+(h/2)*q1,z[i]+(h/2)*q2,t[i]+(h/2))
    r2=f2(y[i]+(h/2)*q1,z[i]+(h/2)*q2,t[i]+(h/2))
    s1=f(y[i]+h*r1,z[i]+h*r2,t[i]+h)
    s2=f2(y[i]+h*r1,z[i]+h*r2,t[i]+h)
    y.append(y[i]+(h/6)*(p1+2*q1+2*r1+s1))
    z.append(z[i]+(h/6)*(p2+2*q2+2*r2+s2))
   

print("The value of y(0.4)(calculated numerically)=  ",y[-1])
print("The value of y(0.4)(calculated analytically)=  ",g(0.4))
print("The value of z(0.4)(calculated numerically)=  ",z[-1])
print("The value of z(0.4)(calculated analytically)=  ",g2_(0.4))
m= np.linspace(ti,tf,100000)
plt.plot(m,g(m))
plt.scatter(t,y,c="red")
plt.legend(["Actual y", "RK-4"])
plt.show()
plt.plot(m,g2_(m))
plt.scatter(t,z,c="red")
plt.legend(["Actual z", "RK-4"])
plt.show()
