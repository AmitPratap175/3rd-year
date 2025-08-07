import random
from math import *
num=(input("Enter the number in float format:  "))

l=int(input("Enter the no of bits used:  "))
num=str(num)
    
if(l==16):              #these statements are meant to assign the no of exponent bits and the bias w.r.t the no of bits input
    bit=5
    bias=15
elif(l==32):
    bit=8
    bias=127
elif(l==64):
    bit=11
    bias=1023 
  

rand= (random.randrange(1, l-bit-2, 1)) 

if(num=='0'or num=='+0'):
    print("The binary IEEE 754 conversion is:  ")
    print(str('0 ')+bit*str('0')+str(' ')+(l-bit-1)*str('0'))
    exit()
elif(num=='-0'):
    print("The binary IEEE 754 conversion is:  ")
    print(str('1 ')+bit*str('0')+str(' ')+(l-bit-1)*str('0'))
    exit()
elif(num=='infinity'or num=='+infinity'):
    print("The binary IEEE 754 conversion is:  ")
    print(str('0 ')+bit*str('1')+str(' ')+(l-bit-1)*str('0'))
    exit()
elif(num=='-infinity'):
    print("The binary IEEE 754 conversion is:  ")
    print(str('1 ')+bit*str('1')+str(' ')+(l-bit-1)*str('0'))
    exit()
elif(num=='NaN'):
    print("The binary IEEE 754 conversion is:  ")
    if(rand%2==0):
        print(str('1 ')+bit*str('1')+str(' ')+(rand)*str('0')+(l-bit-1-rand)*str('1'))
    else:
        print(str('0 ')+bit*str('1')+str(' ')+(rand)*str('0')+(l-bit-1-rand)*str('1'))
    exit()
num=float(num)

a=log(abs(num),2)
f=floor(a)

dec=a-f

y=num*(2**-f)

def manbit(f,y):
    mbit=[]
    if(f<=-1022):
        print("It is a subnormal number.")
        for i in range(l-bit-1):
            if(y>=2**(-(i+1))):
                mbit.append(1)
                y=y-2**(-(i+1))
            else:
                mbit.append(0)
                y=y
    else:
        y=y-1.
        print("It is a normal number.")
        for i in range(l-bit-1):
            if(y>=2**(-(i+1))):
                mbit.append(1)
                y=y-2**(-(i+1))
            else:
                mbit.append(0)
                y=y
    mbit = (''.join([str(elem) for elem in mbit]))
    return mbit

#to calculate the binary representation of the exponent bit
def expbit(f):
    e=bias+f
    quo=1
    div=0
    ebit=[]
    while(quo!=0.):
        quo=int(e)/int(2)
        ebit.append(int(e)%2)
        e=quo
    while(len(ebit)<(bit)):
        ebit.append('0')
    ebit=ebit[-1::-1]
    if(len(ebit)>bit):
        ebit=ebit[abs(bit-len(ebit)):]

    ebit = (''.join([str(elem) for elem in ebit]))
    return(ebit)

if(num>0.):
    new_num='0 '+expbit(f)+' '+manbit(f,y)
else:
    new_num='1 '+expbit(f)+' '+manbit(f,y)
if(len(new_num)<(l+2)):
    new_num+=((l+2)-len(new_num))*'0'           #adding zeroes if the length is less than the length 

print("The largest subnormal number:  ",2**(1-bias)*(1.-2**(-(l-bit-1))))
print("The smallest subnormal number:  ",2**(1-bias)*(2**(-(l-bit-1))))
print("The largest normal number:  ",2**(bias)*(2.-2**(-(l-bit-1))))
print("The smallest normal number:  ",2**(1-bias))
print("The binary IEEE 754 conversion is:  ")
print(new_num)

