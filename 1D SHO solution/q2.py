import numpy as np
import matplotlib.pyplot as plt
#potential as a gaussian around x
def V(x):
    if(abs(x)<=2):
        return np.sqrt(2.5/np.pi)*np.exp(-x**2/0.4)

#function to calculate the psi
def qmwell(x,h,psi,E):
    phi0=0
    phi1=0.0001
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
    x,h=np.linspace(-2,2,n,retstep=True)
    psi=np.zeros_like(x)
    p=np.array([0.,0.])
    psi=qmwell(x,h,psi,E)
    p[0]=psi[-1]-psi[0]
    E1=E+0.5
    psi=np.zeros_like(x)
    psi=qmwell(x,h,psi,E1)
    p[1]=psi[-1]-psi[0]
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
#initial guess of E1=0.7
Execute(n,eps,0.7,1)
print("The second eigenvalue is: ")
#initial guess of E2=1
Execute(n,eps,1,2)

