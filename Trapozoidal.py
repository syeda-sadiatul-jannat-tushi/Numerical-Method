import  math
f= lambda x: math.exp(x**2)

a=0
b=1
n=6
h= (b-a)/n
sum= f(a)+f(b)

for i in range(n-1):
   a= a + h
   sum = sum + 2*f(a)

sum = sum*h/2
print(sum)

