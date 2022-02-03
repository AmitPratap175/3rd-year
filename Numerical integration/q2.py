import numpy as np
import math
def f(x):
    if choice==2:
        return 2*x
    elif choice==1:
        return 4*x**3
    elif choice==3:
        return 3*x**2
    elif choice==4:
        return x**9
    
a=float(input("Enter the lower bound of the integral: "))
b=float(input("Enter the upper bound of the integral: "))
choice=int(input("Enter which function to use:  \n1. 4*x**3   \n2. 2*x  \n3.3*x**2  \n4.x**9  :  "))
if choice==2:
        actual=1.
elif choice==1:
        actual=0.1
elif choice==3:
        actual=1.
elif choice==4:
        actual=0.1

h=[]
ans=[]
n=np.array([10**i for i in range(1,6)])
for i in range(5):
    h.append((b-a)/n[i])
    x,k=np.linspace(a,b,n[i]+1,retstep=True)
    arr=np.ones_like(x)
    for j in range(1,np.size(arr)-1):
        if j%2==0:
            arr[j]=2.
        else:
            arr[j]=4.
    s=np.dot(f(x),arr)
    ans.append((h[i]/3)*s)
log_h=np.log10(h)
rel=ans-actual*np.ones_like(ans)
log_rel=np.log10(np.abs(rel))
print("log10(h)\t\tcomputed integral\t\t\tlog10(actual)")
for i in range(5):
    print('%.17f'%log_h[i],"\t\t\t",'%.17f'%ans[i],"\t\t",'%.17f'%log_rel[i])

file = open('output2.dat','a') 
for i in range(5):
    file.write(str('%.17f'%log_h[i]))
    file.write("\t")
    file.write(str('%.17f'%ans[i]))
    file.write("\t")
    file.write(str(log_rel[i]))
    file.write("\n")
file.close() 

