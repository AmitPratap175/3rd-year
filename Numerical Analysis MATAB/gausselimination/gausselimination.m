clear();
a=input("Enter the matrix A:");
b=input("Enter the matrix b input as a row matrix:");
n=size(a);
b=b';
A=[a b];
for j = 1:(n(1)-1)
        for i= (j+1) : n(1)
            mult = A(i,j)/A(j,j) ;
            for k= j:n(1)+1
                A(i,k) = A(i,k) - mult*A(j,k); 
            end
        end
end
x=[];
x(n(1))= A(n(1),n(1)+1)/A(n(1),n(1));
for l= n(1)-1:-1:1
    temp=0;
    for m=l+1:n(1)
        temp=temp-A(l,m)*x(m);
    end
    x(l)=(A(l,n(1)+1)+temp)/A(l,l);
end
x      

