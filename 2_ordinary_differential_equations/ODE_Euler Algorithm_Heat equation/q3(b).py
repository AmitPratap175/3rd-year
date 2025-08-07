import numpy as np
import matplotlib.pyplot as plt

#final and initial values assignment
ti=0
tf=10.
#the x values are divided and stored
x,h=np.linspace(0,1,100,retstep=True)
dt=0.000052
t=ti
#initial us are calculated and stored.
us= np.where(x<0.5,x,1-x)
line,=plt.plot(x,us)
#x and y labels
plt.xlabel('x')
plt.ylabel('Heat')
#animating
while t<tf:
    us[1:-1]+=(dt/h**2)*(us[:-2]+us[2:]-2*us[1:-1])
    t+=dt
    line.set_ydata(us)
    plt.title('t='+str('%.6f'%t))
    plt.pause(0.0001)

plt.show()
