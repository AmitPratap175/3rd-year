num=input("Enter the number in binary format:  ")
l=len(num)
if(l==16):
    bit=5
    bias=15
elif(l==32):
    bit=8
    bias=127
elif(l==64):
    bit=11
    bias=1023
else:
    print("The entered number is incorrect!!!")
    exit()

arr=list(map(int,list(num)))
arr_sign=arr[0]
arr_exp=arr[1:bit+1]
arr_man=arr[bit+1:]
exp=0.
man=0.
if arr_sign==0:
    char='+'
else:
    char='-'
for i in range(bit):
    exp+=arr_exp[bit-i-1]*2**(i)
for i in range(l-bit-1):
    man+=arr_man[i]/2**(i+1)
if(exp==0 and man==0):
    print("Entered number in floating point value is:  ",str(char)+str(0))
elif(exp==0 and man!=0):
    print("Entered number in floating point value is:  ",(-1)**(arr_sign)*2**(1-bias)*(man))
elif(exp==(2**(bit)-1) and man==0):
    print("Entered number in floating point value is:  ",str(char)+str('infinity'))
elif(exp==(2**(bit)-1) and man!=0):
    print("Entered number in floating point value is:  ",str('NaN'))
else:
     print("Entered number in floating point value is:  ",(-1)**(arr_sign)*2**(exp-bias)*(1.+man))
