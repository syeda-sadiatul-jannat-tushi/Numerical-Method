import  math
f= lambda x,y: x

x0=0
y0=0
xn=1
h=0.5

steps= int((xn-x0)/h)

for i in range(steps):
   y1=y0+h*f(x0,y0)
   x1=x0+h
   y1=y0+(h/2)*(f(x0,y0)+f(x1,y1))
   y0=y1
   x0=x1

print(y1)

