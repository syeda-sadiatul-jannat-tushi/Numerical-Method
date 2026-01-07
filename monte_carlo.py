import numpy as np

f= lambda x:3*(x**2)+1
a=0
b=2
n=100
u=np.random.uniform(0,1,n)

sum=0

for i in range(n):
    x= a+(b-a)*u[i]
    sum = sum + f(x)

avg= sum/n
l=(b-a)*avg
print(l)
