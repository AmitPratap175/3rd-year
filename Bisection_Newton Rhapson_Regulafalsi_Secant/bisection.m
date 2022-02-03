clear
format longEng
tol=input("Enter the error bound:");
l=input("Enter value of a:");
r=input("Enter value of b:");
fprintf("\nThe computed root using bisection method is:\n")
bisect(l,r,tol);
fprintf("\nThe computed root using regula-falsi method is:\n")
regula(l,r,tol);
fprintf("\nThe computed root using Newton Raphson method is:\n")
x0=input("Enter the estimate of the root:");
newtonr(x0,tol);
fprintf("\nThe computed root using Secant method is:\n")
xs(1)=r;
xs(2)=l;
secantm(xs,tol);

function maxiter=max()
    global maxiter
    maxiter= 100;
end

function bisect(l,r,tol)
    format longEng
    if (f(l)*f(r))>0.
        fprintf("\nThere is no root in the interval provided!!!\n\n")
        return;
    end
    c=l;
    i=1;
    while abs(f(c(end)))>tol
        c(i)=(l(i)+r(i))./2;
        if f(c(i))==0
            disp(c(i));
            break;
        elseif (f(c(i))*f(r(i)))<0.
            l(i+1)=c(i);
            r(i+1)=r(i);
        else 
            r(i+1)=c(i);
            l(i+1)=l(i);
        end
        if i>max()
            fprintf("\nCouldn’t converge to the solution in %d steps.\n\n",max())
            return;
        end
        i=i+1;
    end
    if abs(c(end)-pi/2)<10e-3
        fprintf("\nThere is no root in the interval provided!!!\n\n")
        return;
    end
    k=[1:i-1];
    l=l(1:i-1);
    r=r(1:i-1);
    T=table(k',c',(f(c))','VariableNames',{'n','c','f(c)'})
    fprintf("\nThe final computed root is: %f\n\n",c(end))
    fprintf("\nThe total number of iterations used is: %d\n\n",k(end))
    
end
function regula(l,r,tol)
    format longEng
    i=3;
    c(1)=l;
    c(2)=r;
    if (f(l)*f(r))>0.
        fprintf("\nThere is no root in the interval provided!!!\n\n")
        return;
    end
    while abs(f(c(end)))>tol
        c(i)=r-(f(r)*((r-l)/(f(r)-f(l))));
        if f(l)*f(c(i))>0
            l=c(i);
        end
        i=i+1;
        if i>max()+3
            fprintf("\nCouldn’t converge to the solution in %d steps.\n\n",max())
            return;
        end
    end
    if abs(c(end)-pi/2)<10e-3
        fprintf("\nThere is no root in the interval provided!!!\n\n")
        return;
    end
    xi=[0 c(2:end)-c(1:end-1)];
    n=[1:i-1];
    T=table(n',c',(f(c))','VariableNames',{'n','x_n','f(x_n)'})
    fprintf("\nThe final computed root is: %f\n\n",c(end))
    fprintf("\nThe total number of iterations used is: %d\n\n",n(end))
end

function newtonr(x0,tol)
    format longEng
    i=1;
    while abs(f(x0(end)))>=tol
        x0(i+1)=x0(i)-(f(x0(i))/f_(x0(i)));
        i=i+1;
        if i>max()+1
            fprintf("\nCouldn’t converge to the solution in %d steps.\n\n",max())
            return;
        end
    end
    if abs(x0(end)-pi/2)<10e-3
        fprintf("\nThere is no root in the interval provided!!!\n\n")
        return;
    end
    
    n=[0:i-1];
    T=table(n',x0',(f(x0))','VariableNames',{'n','x_n','f(x_n)'})   
    fprintf("\nThe final computed root is: %f\n\n",x0(end))
    fprintf("\nThe total number of iterations used is: %d\n\n",n(end))
end

function secantm(x0,er)
    format longEng
    i=2;
    while abs(f(x0(end)))>=er
        x0(i+1)=x0(i)-(f(x0(i))*((x0(i)-x0(i-1))/(f(x0(i))-f(x0(i-1)))));
        i=i+1;
        if i>max()+2
            fprintf("\nCouldn’t converge to the solution in %d steps.\n\n",max())
            return;
        end
    end
    if abs(x0(end)-pi/2)<10e-3
        fprintf("\nThere is no root in the interval provided!!!\n\n")
        return;
    end
    
    n=[0 0:i-2];
    T=table(n',x0',(f(x0))','VariableNames',{'n','x_n','f(x_n)'})
    fprintf("\nThe final computed root is: %f\n\n",x0(end))
    fprintf("\nThe total number of iterations used is: %d\n\n",n(end))
end

function f=f(x)
    f=x-(1/3)*tan(x);
end

function f=f_(x)
        f=1-(1/3)*(sec(x))^2;
end
