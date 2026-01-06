import  math
f= lambda x: x**3-2

a=0
b=6
n= 12
h= (b-a)/n
sum= f(a)+f(b)

for i in range(1,n):
   a= a + h

   if i%2==0:
      sum= sum+ (2*f(a))
   else:
      sum = sum+(4*f(a))

sum = sum*h/3
print("Approximation of integral=", sum)

