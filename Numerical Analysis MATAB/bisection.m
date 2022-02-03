clear
er=input("Enter the error bound:");
a=input("Enter value of a:");
b=input("Enter value of b:");
bisect(a,b,er);
function bisect(a,b,er)
    n=real(ceil((log((a-b)./er)/log(2))));
    for i=1:n
        c(i)=(a(i)+b(i))./2;
        if f(c(i))==0
            disp(c(i));
            break;
        elseif (f(c(i))*f(b(i)))<0.
            a(i+1)=c(i);
            b(i+1)=b(i);
        else 
            b(i+1)=c(i);
            a(i+1)=a(i);
        end
    end
    k=[1:n];
    a=a(1:n);
    b=b(1:n);
    T=table(k',a',b',c',b'-c',(f(c))','VariableNames',{'n','a','b','c','b-c','f(c)'})

    x=[a:0.0001:b];
    y=f(x);
    axis on;
    plot(x,y,'LineWidth',2), xlabel('x'), ylabel('f(x)');
    grid on;
    line([1,1], ylim, 'Color', 'k', 'LineWidth', 2); 
    line(xlim, [0,0], 'Color', 'k', 'LineWidth', 2); 
    hold on;
    sz=500;
    for i=1:n
        h1=scatter(c(i),0,sz,'.','r');
        pause(2);
        if i~=n
            delete((h1));
        end
    end
    function f=f(x)
        f=x.^6-x-1;
    end
end





    

