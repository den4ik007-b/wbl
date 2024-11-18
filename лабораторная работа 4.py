str = input("Введите строку  ")
x = len(str)
for i in range(x):
    if str[i] == 'к' or str[i] == 'з':
        print(str(i))

