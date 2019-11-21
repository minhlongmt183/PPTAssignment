import math
from sympy import *
#we have to create a "symbol" called x
#De bai
x=Symbol('x')
f=exp(x)+2**-x + 2*cos(x)-6
a= 1
b= 2

#Chon x0
temp=f
f1=f.diff()
f2=f1.diff()
f=lambdify(x,f)
f1=lambdify(x,f1)
f2=lambdify(x,f2)
if f(a)*f2(a)>=0:
    x0=a
if f(b)*f2(b)>=0:
    x0=b

#xac dinh m
if abs(f1(a))>abs(f1(b)):
    m=abs(f1(b))
else:
    m=abs(f1(a))
print(m)
#Tim nghiem bang phuong phap NewTon

eps=pow(10,-6)
err=eps+1
N=100
i=0
denta=0
print(i,"\t",x0)
i=i+1
while i<N and err>eps:
    f=temp
    f_prime=f.diff()

    f=lambdify(x,f)
    f_prime=lambdify(x,f_prime)

    x1=x0-f(x0)/f_prime(x0)
    err=abs(f(x1)/m)
    print(i,"\t",x1,"\t",err)
    x0=x1
    i=i+1
