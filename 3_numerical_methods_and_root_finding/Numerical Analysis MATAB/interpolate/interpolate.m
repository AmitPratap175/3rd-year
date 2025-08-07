
x=[0 1 3];
y=[1 0 -8];
x1=input("Enter the value of x:");
fprintf("The value using Lagrange's Interpolation formula:%d\n",f(x1,x,y))
d=fdivided(x,y);
fprintf("The value using newton's divided difference:%d\n",fdiv_inter(x1,x,d))
x2=[-1:0.0001:10];
y2=zeros(1,length(x2));
y3=zeros(1,length(x2));
for i=1:length(x2)
    y2(i)=f(x2(i),x,y);
    d=fdivided(x,y);
    y3(i)=fdiv_inter(x2(i),x,d);
end
plot(x2,y3,'.r','MarkerSize',15);
hold on;
plot(x2,y2,'b','MarkerSize',10);
hold on;
sz=300;
scatter(x,y,sz,'b');
legend('Lagrange','Newton divided','actual points');

    
function f=f(x1,x,y)
    m=length(x);
    f=0;
    for i=1:m
        k=1;
        for j=1:m
            if j~=i
                k=k*((x1-x(j))/(x(i)-x(j)));
            end
        end
        f=f+k*y(i);
    end
end
function val=fdiv_inter(x1,x,d)
    val=0;
    m=length(x);
    for i=1:m
        k=1;
        for j=2:i
            k=k*(x1-x(j-1));
        end
        val=val+k*d(i);
    end
end
    
function d=fdivided(x,y)
    d=y;
    m=length(x);
    for i=2:m
        for j=m:-1:i
            d(j)=(d(j)-d(j-1))/(x(j)-x(j-i+1));
        end
    end
end


