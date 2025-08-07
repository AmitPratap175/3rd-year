clear;
%f(x)=exp(-x^2)
a=[0 0 0];
b=[1 4 2*pi];

choice=input("Enter your choice:(1 for function 1, 2 for function 2, 3 for function 3):");
calc_val=[];
true_val=[0.7468241328124271 atan(4) 2*pi/sqrt(3)];
n=[];
for j=[1:7]  
    n(j)=2^j;
    val=0;
    xi=a(choice);
    h=(b(choice)-a(choice))/n(j);
    for i=[1:(n(j)/2)]
        val= val+simps(xi,xi+(2)*h,h,choice);
        xi=xi+2*h;
    end
    calc_val(j)=val;
end
format shortEng;
err = abs(calc_val-true_val(choice));
ratio=[0];
for i=[2:7]
    ratio(i)=err(i-1)/err(i);
end
I1=table(n',(err)',ratio','VariableNames',{'n','Error','ratio'})

function v=simps(x,y,h,ch)
    c=(x+h);
    switch ch
        case 1
            v = (h/3)*(f(x)+4*f(c)+f(y));
        case 2
            v = (h/3)*(f2(x)+4*f2(c)+f2(y));
        case 3
            v = (h/3)*(f3(x)+4*f3(c)+f3(y));
    end
end

function f=f(x)
    f=exp(-x^2);
end

function f=f2(x)
    f=1/(1+x^2);
end

function f=f3(x)
    f=1/(2+cos(x));
end