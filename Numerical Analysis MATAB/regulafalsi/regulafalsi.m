clear
a=input("Enter the estimate of the root:");
b=input("Enter the second(larger) estimate of the root:");
er=input("Enter the error bound:");
regula(a,b,er);
function regula(a,b,er)
    i=3;
    c(1)=a;
    c(2)=b;
    while abs(f(c(end)))>er
        c(i)=b-(f(b)*((b-a)/(f(b)-f(a))));
        if f(a)*f(c(i))>0
            a=c(i);
        end
        i=i+1;
    end
    xi=[0 c(2:end)-c(1:end-1)];
    n=[0:i-2];
    T=table(n',c',(f(c))',xi','VariableNames',{'n','x_n','f(x_n)','x_n-x_(n-1)'})
    
    x1=[1:0.00001:1.7];
    y=f(x1);
    axis on;
    plot(x1,y,'LineWidth',2), xlabel('x'), ylabel('f(x)');
    grid on;
    line([1,1], ylim, 'Color', 'k', 'LineWidth', 2); 
    line(xlim, [0,0], 'Color', 'k', 'LineWidth', 2); 
    hold on;
    sz=500;
    for j=1:i-1
        h1=scatter(c(j),0,sz,'.','r');
        pause(1);
        if j~=i-1
            delete((h1));
        end
    end
        

    function f=f(x)
        f=x.^6-x-1;
    end
end
