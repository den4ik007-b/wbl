n = int(input("Введите количество элементов списка -> "))
x = []


for i in range (n):
    x.append(int(input(f"Введите элемент {i} -> ")))
    if (x[i])//2:
        print(x[i])
print("Исходный список: ", x)




