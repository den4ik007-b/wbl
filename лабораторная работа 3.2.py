import math
from math import cos

x=int (input("Введите x:  "))
x1= 0
xn= 2
dx= 0.1
a= 2.1
b= 0.3
y=0
while x1<=xn:
    y += (math.cos(a*x**2))/(1+pow(math.tan(b*x),3))
x1 += x1+dx
print(y)
