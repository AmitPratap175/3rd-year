import numpy as np
from scipy.stats import maxwell
import matplotlib.pyplot as plt

##M_E=5.972e24
##M_M=6.39e23 
v_E=11.186  #escape velocity of earth
v_M=5.03    #escape velocity of mars
T_E=287.15  #the average surface temperature of the earth
T_M=210.372     #the average surface temperature of mars
k=1.380649e-23      # units: J-K^-1

def f(m,x,T):
    return ((m/(2*np.pi*k*T))**1.5)*np.exp(-(m*x**2/(2*k*T)))

def start():
    ch=int(input("Enter the choice:\n1.Earth and Hydrogen molecule \n2.Earth and Oxygen molecule\n3.Mars and Hydrogen molecule\n4.Mars and Oxygen molecule\nEnter : "))
    if ch==1:
        m=2*1.6735e-27
        T=T_E
        v=v_E
    elif ch==2:
        m=5.31e-26
        T=T_E
        v=v_E
    elif ch==3:
        m=2*1.6735e-27
        T=T_M
        v=v_M
    elif ch==4:
        m=5.31e-26
        T=T_M
        v=v_M
    else:
        start()
    M=1000      #the number of times we run the simulation learns
    p =np.zeros(M)  #the probabilities are stored in this matrix
    N=100000        #the number of divisions made
    x0=(v*1000)     # the escape  velocity
    for ii in range(M):
        x=maxwell.rvs(scale=np.sqrt(k*T/m),size=N)
        
        if ii==1:
            plt.xlim(0,x0+1000)
            y = np.arange(0,N)
            plt.hist(x,bins=70,density=True,label='random maxwell distribution')
            z=maxwell.pdf(y, scale=np.sqrt(k*T/m))
            plt.plot(z,label='Maxwell pdf')
            plt.axvline(x=x0,color='r',label='escape velocity')
        #x=np.random.randn(N)*np.sqrt(k*T/m)#*((m/(2*np.pi*k*T)))
        #print(np.var(x))
        p1=np.sum(abs(x)>x0)/N
        #p2=np.sum(x*x<=x0*x0)/N
        p[ii]=p1
    print('The probability of the particle escaping is: ',np.mean(p))#the probability is printed
start()
plt.legend(loc='best')
plt.show()
