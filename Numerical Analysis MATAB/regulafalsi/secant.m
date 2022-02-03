clear
x0=input("Enter the estimate of the root:");
x0(2)=input("Enter the second(smaller) estimate of the root:");
er=input("Enter the error bound:");
secantm(x0,er);
function secantm(x0,er)
    i=2;
    while abs(f(x0(end)))>=er
        x0(i+1)=x0(i)-(f(x0(i))*((x0(i)-x0(i-1))/(f(x0(i))-f(x0(i-1)))));
        i=i+1;
    end
    xi=[0 x0(2:end)-x0(1:end-1)];
    n=[0:i-1];
    T=table(n',x0',(f(x0))',xi','VariableNames',{'n','x_n','f(x_n)','x_n-x_(n-1)'})
    
    x1=[1:0.00001:1.7];
    y=f(x1);
    axis on;
    plot(x1,y,'LineWidth',2), xlabel('x'), ylabel('f(x)');
    grid on;
    line([1,1], ylim, 'Color', 'k', 'LineWidth', 2); 
    line(xlim, [0,0], 'Color', 'k', 'LineWidth', 2); 
    hold on;
    sz=500;
    for j=1:i
        h1=scatter(x0(j),0,sz,'.','r');
        pause(2);
        if j~=i
            delete((h1));
        end
    end
        

    function f=f(x)
        f=x.^6-x-1;
    end
end
