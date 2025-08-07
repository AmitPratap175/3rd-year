import numpy as np
import matplotlib.pyplot as plt
#harmonic oscillator potential
def V(x):
        return 0.5*x**2

#function to calculate the psi
def qmwell(x,h,psi,E):
        #shooting method used
    a=np.sqrt(2*V(x[-1])-E)
    phi0=np.exp(a*x[0])
    phi1=np.exp(a*x[1])
    psi[1]=phi1
    f=2*(V(x[0])-E)
    for i in range(2,n):
        phi2=h**2*f*psi[i-1]+2*phi1-phi0
        phi0=phi1
        phi1=phi2
        f=2*(V(x[i])-E)
        psi[i]=phi1/(1-f*h**2/12.)
    return psi
#function to calculate the E values and consequently calculate the functions
def Execute(n,eps,E,m):
    x,h=np.linspace(-5,5,n,retstep=True)
    psi=np.zeros_like(x)
    p=np.array([0.,0.])
    psi=qmwell(x,h,psi,E)
    p[0]=psi[-1]-psi[0]
    E1=E+0.5
    psi=np.zeros_like(x)
    psi=qmwell(x,h,psi,E1)
    p[1]=psi[-1]-psi[0]
    #bisection method used
    while(abs(p[1])>eps):
        if(p[0]*p[1]<0):
            E2=0.5*(E+E1)
            psi=np.zeros_like(x)
            psi=qmwell(x,h,psi,E2)
            if (p[0]*(psi[-1]-psi[0])<0):
                p[1]=psi[-1]-psi[0]
                E1=E2
            else:
                p[0]=psi[-1]-psi[0]
                E=E2
        else:
            E1=E+0.5
            psi=np.zeros_like(x)
            psi=qmwell(x,h,psi,E1)
            p[1]=psi[-1]-psi[0]
    # printing the calculated E values      
    print(E1)
    plt.plot(x,((-1)**(m+1))*psi/np.linalg.norm(psi))
    '''if m%2==0:
        plt.plot(x,np.sin(m*np.pi*x/2)/np.linalg.norm(np.sin(m*np.pi*x/2)))
    else:
        plt.plot(x,np.cos(m*np.pi*x/2)/np.linalg.norm(np.sin(m*np.pi*x/2)))
    plt.legend(['Calculated','Theoretical'])'''
    plt.xlabel('x')
    plt.ylabel('$\psi$')
    plt.show()
    

n=int(input("Enter the order n= "))
eps=float(input("Enter the tolerance in the Energy: "))
print("The first eigenvalue is: ")
#initial guess of E1=0.4
Execute(n,eps,0.4,1)
print("The second eigenvalue is: ")
#initial guess of E2=1.4
Execute(n,eps,1.4,2)

