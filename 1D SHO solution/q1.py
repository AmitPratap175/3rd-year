import numpy as np
import matplotlib.pyplot as plt

#function for using the numerov 
def qmwell(x,h,psi,k,E):
        psi[1]=1+k
        psi[0]=1.
        f = - 2*E
        #for i in range(2,n):
        #  psi[i]=-(psi[i-1]*(5*h**2*np.pi**2/24-2)+psi[i-2]*(1+h**2*np.pi**2/48)+h**2*np.pi**2/4)/(1+h**2*np.pi**2/48)
        phi0=psi[0]
        phi1=psi[1]
        for i in range(2,n):
                phi2=h**2*f*psi[i-1]+2*phi1-phi0
                phi0=phi1
                phi1=phi2
                psi[i]=phi1/(1-(f*h**2)/12.)
        return psi

# function for calculating 
def Execute(n,eps,k,E):
        x,h=np.linspace(0,1,n,retstep=True)
        psi=np.zeros_like(x)
        psi=qmwell(x,h,psi,k,E)
        
        P1= psi[-1]
        E1=E+0.2
        psi=qmwell(x,h,psi,k,E)
        P2= psi[-1]
        
        while abs(P2-2.)>eps:
                if (P1-2.)*(P2-2.)<0:
                        E2=0.5*(E+E1)
                        psi=qmwell(x,h,psi,k,E2)
                        P3=psi[-1]
                        if (P1-2.)*(P3-2.)<0:
                                E1=E2
                                P2=P3
                        else:
                            P1=P3
                            E=E2
                else:
                        E1=E1+0.2
                        psi=qmwell(x,h,psi,k,E1)
                        P2=psi[-1]
        #for updating the initial guess of the psi[1]
        while((psi[-1]-2)>0 and abs(psi[-1]-2)>eps):
                k=k-1e-6
                psi=qmwell(x,h,psi,k,E)
        while((psi[-1]-2)<0 and abs(psi[-1]-2)>eps):
                k=k+1e-6
                psi=qmwell(x,h,psi,k,E)
        #plotting the psi and analytical solution together
        plt.plot(x,psi-1)
        plt.plot(x,(2*np.sin(np.pi*x*0.5)+np.cos(np.pi*x*0.5)-1),'--')
        plt.legend(['Calculated','Theoretical'])
        plt.show()
    

n=int(input("Enter the number of divisions: "))
eps=float(input("Enter the tolerance: "))
h=1/(n-1)
k=3.14*h
Execute(n,eps,k,1)


