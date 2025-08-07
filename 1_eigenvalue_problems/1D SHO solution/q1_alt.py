import numpy as np
import matplotlib.pyplot as plt

def V(x):
    if abs(x)>0.5:
        return 0
    else:
        return 10

def qmwell(x,h,psi,k):
        E=7.6056
        psi[1]=k
        psi[0]=0
        f = - 2*(E-V(x[0]))
        #for i in range(2,n):
        #  psi[i]=-(psi[i-1]*(5*h**2*np.pi**2/24-2)+psi[i-2]*(1+h**2*np.pi**2/48)+h**2*np.pi**2/4)/(1+h**2*np.pi**2/48)
        phi0=psi[0]
        phi1=psi[1]
        for i in range(2,n):
                phi2=h**2*f*psi[i-1]+2*phi1-phi0
                phi0=phi1
                phi1=phi2
                f=2*(V(x[i])-E)
                psi[i]=phi1/(1-(f*h**2)/12.)
        return psi

def Execute(n,eps,k):
    x,h=np.linspace(-1,1,n,retstep=True)
    psi=np.zeros_like(x)
    psi=qmwell(x,h,psi,k)
    print(psi[1])
    while((psi[-1])>0 and abs(psi[-1])>eps):
        k=k-1e-6
        psi=qmwell(x,h,psi,k)
    while((psi[-1])<0 and abs(psi[-1])>eps):
        k=k+1e-6
        psi=qmwell(x,h,psi,k)
    plt.plot(x,psi/np.linalg.norm(psi))
    #plt.plot(x,(2*np.sin(np.pi*x*0.5)+np.cos(np.pi*x*0.5)-1),'--')
    plt.legend(['Calculated','Theoretical'])
    plt.show()
    

n=int(input("Enter the order n= "))
eps=1e-4
h=1/(n-1)
k=0.7*h
Execute(n,eps,k)


