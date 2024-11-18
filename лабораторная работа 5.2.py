n = int(input("Введите количество элементов списка -> "))
m = 10
x = []
y = []

for i in range (n):
    x.append(int(input(f"Введитеэлемент {i} -> ")))
    if abs(x[i])<m:
        y.append(x[i])

print("Исходный список: ", x)
print("Новый список: ", y)

