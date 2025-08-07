import numpy as np
from math import *
import matplotlib.pyplot as plt

fi=open('1(a).dat','w')
#initial and final values are assigned
t=0.
tf=100
h=0.01
#no of divisions to be made calculated which is just 1 shorter so we add n+1 later while dividing the t values
n=ceil((tf-t)/h)
t=np.linspace(t,tf,n+1)
#q and p of the same dimensions as t are created having all the elemnts 0.
q=np.zeros_like(t)
p=np.zeros_like(t)
#initial q and p values
q[0]=1
p[0]=0
#updating the q values subsequently
for i in range(n):
    q[i+1]=q[i]+p[i]*h
    p[i+1]=p[i]-q[i]*h
    print(t[i],q[i],p[i],file=fi)
#plotting the required values    
plt.plot(t,0.5*(p**2+q**2))
#plt.plot(t,q,t,p)
plt.ylabel('($p^2$+$q^2$)$/2$')
plt.xlabel('t')
#plt.ylim(-1,1)
plt.show()
fi.close()
