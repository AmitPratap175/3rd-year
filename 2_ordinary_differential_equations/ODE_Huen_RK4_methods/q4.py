import numpy as np
from math import *
import matplotlib.pyplot as plt

def f(y,x):
    return -0.6*y+10*exp(-(x-2)**2/(2*(0.075)**2))
def g(x):
    return (5*np.exp(x)-3)*np.exp(-2*x)
def rk4(tf,ti,h):
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


    print("The value of y(0.4)(calculated numerically)=  ",y[-1])
    #print("The value of y(0.4)(calculated analytically)=  ",g(0.4))

    m= np.linspace(ti,tf,100000)
    #plt.plot(m,g(m))
    plt.plot(t,y)
    plt.legend(["Actual", "RK-4"])
    plt.show()
    return y,t,n

ti=0.
tf=4
h=[0.1, 0.05]
y1,t1,n1=rk4(tf,ti,h[0])
y2,t2,n2=rk4(tf,ti,h[1])
print(y1)
err=[]
x=[]
for i in range(n1+1):
    for j in range(n2+1):
        if(t1[i]==t2[j]):
            err.append(abs(y1[i]-y2[j]))
            x.append(t1[i])
plt.plot(x,err)
plt.show()

"""file = open('output.dat','a') 
for i in range(1,len(x)):
    file.write(str('%.10f'%(log10(x[i]))))
    file.write("\t")
    file.write(str('%.17f'%(log10(err[i]))))
    file.write("\n")
file.close() 
"""
