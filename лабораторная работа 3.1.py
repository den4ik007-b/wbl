import math

x=int(input("Введите x:  "))
x1= 0
xn= 2
dx= 0.1
a= 2.1
b= 0.3
y=0
for x1 in range(x1, xn, dx):
    y += (math.cos(a * x ** 2)) / (1 + pow(math.tan(b * x), 3))
print(y)
