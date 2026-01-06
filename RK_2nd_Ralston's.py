import  math
f= lambda x,y: x+y

x0=0
y0=1
xn=0.1
h=0.05

steps= int((xn-x0)/h)

for i in range(steps):
   k1=f(x0,y0)
   k2=f(x0+3*h/4, y0+3*h/4*k1)
   y1=y0+h/3*(k1+2*k2)

   y0=y1
   x0=x0+h

print(y1)

