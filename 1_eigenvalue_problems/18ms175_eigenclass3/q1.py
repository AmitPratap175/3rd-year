import numpy as np
import matplotlib.pyplot as plt
def V(x):
    return 0

def H(n):
    H=np.zeros((n,n),dtype=float)
    x=np.array([i+1 for i in range(n)])
    h=1.
    for i in range(n):
        for j in range(n):
            if i==j:
                H[i][j]=V(x[i])+1/h**2
            elif(abs(i-j)==1):
                H[i][j]=-0.5/h**2
    H[0][n-1]=-0.5/h**2
    H[n-1][0]=-0.5/h**2
    return H
n=1000
val=np.linalg.eigh(H(n))
print(val[0])
#exact=np.array([i**2/2 for i in range(0,n,2)])
#print(exact)
#print(10e5*val[0][::2]-exact)

