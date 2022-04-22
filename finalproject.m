%Part1 

%physcal units of E0 are N/m^2
%a is dimensionless
%Taylor series: E_0*eps-->Hooke's law





%Part 2

m=load('stressstrain.m');
stress=m(:,1);
strain=m(:,2);

m1=mean(stress);
m2=mean(strain);

disp(m1);
disp(m2);

%Newton-Raphson
DELTA=10^(-8);

disp('Newton-Raphson Method');
a=input('what is your intial guess for the root?'); 
%input 30

count=0;
max=100;

  
while (abs(f(a,m1,m2))>=DELTA) 

r = f(a,m1,m2)/g(a,m2); 
a = a - r;

count=count+1;
if (count >= max) 
    break; 
end
end


disp('The value of the root is :');
disp(a);

disp('Number of iterations:');
disp(count); 





%Part 3

n=length(stress);
for i=2:n
    derivative(i)=(stress(i)-stress(i-1))/(strain(i)-strain(i-1));
end

d=derivative;

figure(1)
plot(stress, d,'ro');
%do not need to include






%Part 4

x=stress(6:n);
y=d(6:n);

%least square
sumx=0;
sumy=0;
sumxy=0;
sumx2=0;

for i=1:n-6
    sumx=sumx+x(i); 
    sumy=sumy+y(i); 
    sumxy=sumxy+x(i)*y(i);
    sumx2=sumx2+x(i)*x(i);
end

xm=sumx/(n-6); 
ym=sumy/(n-6); 
a1=((n-6)*sumxy-sumx*sumy)/((n-6)*sumx2-sumx*sumx); 
a0=ym-a1*xm; 

st=0;
sr=0;

for i=1:n-6
    st=st+(y(i)-ym)*(y(i)-ym); 
    sr=sr+(y(i)-a1*x(i)-a0)*(y(i)-a1*x(i)-a0);
end

r2=(st-sr)/st; 

disp(r2);
disp(a0);
disp(a1); 

figure(2)
plot(x,y,'m*',x,a0+a1*x,'b-');
xlabel('σ')
ylabel('dσ/dε')
title('linear regression of (σ,dσ/dε)')




%Part5

E0=a0; 
a=a1;
%e5=0:0.005:.9;
s5=E0/a*(exp(a*strain)-1);

figure(3)
plot(strain,stress,'bo',strain,s5,'r-');
hold on





%Part 6 

%a=a1;
%e6=0:0.005:.9;
s6=m1/(exp(a*m2)-1)*(exp(a*strain)-1);

%figure(4)
plot(strain,s6,'m-');
hold off

legend('original data','calculated E0','eliminating E0')
xlabel('strain')
ylabel('stress')
title('comparing fit')




%functions

function func=f(a,m1,m2)
sig=m1;
eps=m2;
E0=1;
func=(E0/a)*(exp(a*eps)-1)-sig;
end

function der=g(a,m2)
eps=m2;
E0=1;
der=E0/a^2*(exp(a*eps)-1)+E0/a*eps*exp(a*eps);
end


