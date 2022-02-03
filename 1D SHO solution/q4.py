import numpy as np
import matplotlib.pyplot as plt
n=int(input("Enter the number of divisions(the given question has n=400(20 x 20)): "))
#m is the number of lattice points on each side
m=int(np.sqrt(n))
#unit spacing
dx=1.

H=-4*np.identity(n)
for i in range(n-1):
    if (i+1)%m!=0:
        H[i,i+1]=1
        H[i+1,i]=1
for i in range(n-1):
    if i%m==0:
        H[i,i+m-1]=1
        H[i+m-1,i]=1
for i in range(n-m):
    H[i,i+m]=1
    H[i+m,i]=1
for i in range(n-m*(m-1)):
    H[i,i+(m*(m-1))]=1
    H[i+(m*(m-1)),i]=1
H= -0.5*H/(dx**2)
val=np.linalg.eigh(H)
print ("The eigenvalues are: ")
for i in range(n):
    print ("%d th eigenvalue is : "%(i+1), val[0][i])
    #print ("\n%d th eigenvector is : "%(i+1), val[1][i])
N=np.linspace(1,n,n)
xeval = []
for i in range(m):
    for j in range(m):
        xeval.append((i *2 + j *2) * np.pi ** 2 / 200)

xeval.sort()
plt.scatter(N,xeval)
plt.scatter(N,val[0])
plt.legend(['Actual solution','Calculated Solution'])
plt.xlabel('N')
plt.ylabel('Energy values')
plt.show()


