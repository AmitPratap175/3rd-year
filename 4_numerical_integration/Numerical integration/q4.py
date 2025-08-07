import numpy as np
import math
def f(x):
        return 5*x**4

a=float(input("Enter the lower bound of the integral: "))
b=float(input("Enter the upper bound of the integral: "))
actual=1.

h=[]
ans=[]
n=np.array([10**i for i in range(1,6)])
for i in range(5):
    x,k=np.linspace(a,b,n[i],retstep=True)
    h.append(k)
    arr=np.ones_like(x)
    arr[0]=0.5
    arr[-1]=0.5
    s=np.dot(f(x),arr)
    ans.append(h[i]*s)
log_h=np.log10(h)
rel=ans-actual*np.ones_like(ans)
log_rel=np.log10(np.abs(rel))
print("log10(h)\t\tcomputed integral\t\t\tlog10(actual)")
for i in range(5):
    print(log_h[i],"\t\t",'%.17f'%ans[i],"\t\t",'%.17f'%log_rel[i])

file = open('output4_1.dat','a') 
for i in range(5):
    file.write(str(log_h[i]))
    file.write("\t")
    file.write(str('%.17f'%ans[i]))
    file.write("\t")
    file.write(str(log_rel[i]))
    file.write("\n")
file.close()


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

file = open('output4_2.dat','a') 
for i in range(5):
    file.write(str('%.17f'%log_h[i]))
    file.write("\t")
    file.write(str('%.17f'%ans[i]))
    file.write("\t")
    file.write(str(log_rel[i]))
    file.write("\n")
file.close()


h=[]
ans=[]
n=np.array([10**i for i in range(1,6)])
for i in range(5):
    x,k=np.linspace(a,b,n[i],retstep=True)
    h.append(k)
    arr=np.ones_like(x)
    for j in range(1,np.size(arr)-1):
        if j%3==0:
            arr[j]=2.
        else:
            arr[j]=3.
    s=np.dot(f(x),arr)
    ans.append((3*h[i]/8)*s)
log_h=np.log10(h)
rel=ans-actual*np.ones_like(ans)
log_rel=np.log10(np.abs(rel))
print("log10(h)\t\t\tcomputed integral\t\t\tlog10(actual)")
for i in range(5):
    print(log_h[i],"\t",'%.17f'%ans[i],"\t",'%.17f'%log_rel[i])

file = open('output4_3.dat','a') 
for i in range(5):
    file.write(str(log_h[i]))
    file.write("\t")
    file.write(str('%.17f'%ans[i]))
    file.write("\t")
    file.write(str(log_rel[i]))
    file.write("\n")
file.close() 
