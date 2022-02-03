import numpy as np
from math import *
import matplotlib.pyplot as plt

fi=open('2.dat','w')

t=0.
tf=100
h=0.01
n=ceil((tf-t)/h)
t=np.linspace(t,tf,n+1)
q=np.zeros_like(t)
p=np.zeros_like(t)
q[0]=1
p[0]=0
for i in range(n):
    q[i+1]=q[i]+p[i]*h-0.5*q[i]*h**2
    p[i+1]=p[i]-0.5*(q[i]+q[i+1])*h
    print(t[i],q[i],p[i],file=fi)

q1=np.zeros_like(t)
p1=np.zeros_like(t)
q1[0]=1
p1[0]=0
for i in range(n):
    q1[i+1]=q1[i]+p1[i]*h
    p1[i+1]=p1[i]-q1[i+1]*h
    print(t[i],q1[i],p1[i],file=fi)
    
plt.plot(t,0.5*(p**2+q**2))
plt.plot(t,0.5*np.ones_like(t))
plt.legend(["Calculated","Actual"])
plt.ylabel('0.5*($p^2$+$q^2$)')
plt.xlabel('t')
#plt.ylim(-1,1)
plt.show()
plt.plot(t,q-np.cos(t))
plt.plot(t,q1-np.cos(t))
plt.legend(["Algorithm 2 error","1(b) error"])
plt.ylabel('Error')
plt.xlabel('t')
plt.show()
fi.close()
maxer=np.amax(q-np.cos(t))
print("The maximum error in the algorithms 2 is: ", maxer)
maxer1=np.amax(q1-np.cos(t))
print("The maximum error in the algorithms 1(b) is: ", maxer1)
print("the order of error is (2/1(a)):   ",maxer/maxer1)
#so the error in 1(b) is approximately 12(12.10964444135288) times the error in 2.
