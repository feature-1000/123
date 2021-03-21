import math

def f(x):
    y=math.sin(x)
    return y

a=0
b=math.pi
count=100000
x=[]
for i in range(count):
    x.append(a+i*(b-a)/count)
y=list(map(f,x))

integral=sum(y)
integral=integral-0.5*y[0]-0.5*y[-1]
integral=integral*(b-a)/count 
print(integral)
