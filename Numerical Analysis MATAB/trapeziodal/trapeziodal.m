clear;
%f(x)=exp(-x^2)
a=0;
b=1;


calc_val=[];
true_val=0.7468241328124271;
n=[];
for j=[1:7]  
    n(j)=2^j;
    val=0;
    xi=a;
    h=(b-a)/n(j);
    for i=[1:n(j)]
        val= val+simps(xi,xi+h,h);
        xi=xi+h;
    end
    calc_val(j)=val;
end
format shortEng;
err = abs(calc_val-true_val);
ratio=[0];
for i=[2:7]
    ratio(i)=err(i-1)/err(i);
end
I1=table(n',(err)',ratio','VariableNames',{'n','Error','ratio'})
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear;
a=0;
b=4;

calc_val=[];
true_val=atan(4);
n=[];
for j=[1:7]  
    n(j)=2^j;
    val=0;
    xi=a;
    h=(b-a)/n(j);
    for i=[1:n(j)]
        val= val+simps2(xi,xi+h,h);
        xi=xi+h;
    end
    calc_val(j)=val;
end
format shortEng;
err = abs(calc_val-true_val);
ratio=[0];
for i=[2:7]
    ratio(i)=err(i-1)/err(i);
end

I2=table(n',(err)',ratio','VariableNames',{'n','Error','ratio'})
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear;
a=0;
b=2*pi;

calc_val=[];
true_val=2*pi/sqrt(3);
n=[];
for j=[1:7]  
    n(j)=2^j;
    val=0;
    xi=a;
    h=(b-a)/n(j);
    for i=[1:n(j)]
        val= val+simps3(xi,xi+h,h);
        xi=xi+h;
    end
    calc_val(j)=val;
end
format shortEng;
err = abs(calc_val-true_val);
ratio=[0];
for i=[2:7]
    ratio(i)=err(i-1)/err(i);
end

I3=table(n',(err)',ratio','VariableNames',{'n','Error','ratio'})

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function v=simps(x,y,h)
    v = (h/2)*(f(x)+f(y));
end

function v=simps2(x,y,h)
    v = (h/2)*(f2(x)+f2(y));
end

function v=simps3(x,y,h)
    v = (h/2)*(f3(x)+f3(y));
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