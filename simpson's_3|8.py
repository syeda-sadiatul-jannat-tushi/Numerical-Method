import  math
f= lambda x: x**2

a=0
b=12
n= 6
h= (b-a)/n
sum= f(a)+f(b)

for i in range(1,n):
   a= a + h

   if i%3==0:
      sum= sum+ (2*f(a))
   else:
      sum = sum+(3*f(a))

sum = sum*h*3/8
print("Approximation of integral=", sum)

