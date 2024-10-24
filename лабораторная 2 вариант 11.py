from math import *
import sys
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
msg = "Выберите вид функции f(x): tgh(y) -> 1, sqrt(sin(x)) -> 2, x**y -> 3 "
f = float(input(msg + "\n -> "))
fx = None
s = None
match f:
    case 1:
        fx = tgh(y)
    case 2:
        fx = sqrt(sin(x))
    case 3:
        fx = x**y
case _:
        print("Неверный выбор")
        sys.exit()
if ((x * y) > 0):
    s = tg(fx)+x/cbrt(y)
elif ((x * y) < 0):
    s = ln(fabs(pow(fx,2)*y))
elif :
    s = pow(fx,2)+pow(sin(x),2)
else:
s = "значение не может быть вычислено"
print("Результат: ", s)
