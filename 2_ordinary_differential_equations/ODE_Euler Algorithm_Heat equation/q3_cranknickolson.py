import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sci

ti=0
tf=10.
x,h=np.linspace(0,1,100,retstep=True)
dt=0.000052
t=ti
i=0
us= np.where(x<0.5,x,1-x)

m=(dt/h**2)
line,=plt.plot(x,us)
A = np.array(np.zeros((98,98), dtype = np.float))
B = np.array(np.zeros((98,98), dtype = np.float))
for i in range(98):
    for j in range(98):
        if i==j:
            A[i][j]=(1+m)
            B[i][j]=1-m
        elif abs(i-j)==1:
            A[i][j]=-0.5*m
            B[i][j]=0.5*m


while t<tf:
    us[1:-1]=sci.solve(A,np.dot(B,us[1:-1]))
    t+=dt
    line.set_ydata(us)
    plt.pause(0.0001)

plt.show()
"""while t<tf:
    uis[1:-1]=us[1:-1]+m*(us[:-2]+us[2:]-2*us[1:-1])
    us[1:-1]=0.5*(m/(1-m))*(us[2:]-2*us[1:-1]+us[:-2]+uis[2:]+uis[:-2])
    t+=dt
    line.set_ydata(us)
    plt.pause(0.0001)

plt.show()
"""
