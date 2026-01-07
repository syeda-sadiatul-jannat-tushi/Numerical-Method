import  math
f= lambda x,y: x*y + x**2

x0=0
y0=2
xn=1
h=0.5

steps= int((xn-x0)/h)

for i in range(steps):
   k1=f(x0,y0)
   k2=f(x0+h/2, y0+k1*h/2)
   k3=f(x0+h/2, y0+k2*h/2)
   k4=f(x0+h, y0+h*k3)

   y1= y0+h/6*(k1+2*k2 + 2*k3 + k4)
   y0=y1
   x0=x0+h

print(y1)

