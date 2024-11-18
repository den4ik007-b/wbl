def clean(x):
    return x.replace('-', '').replace('(', '').replace(')', '')


phone_book = ['8(495)430-23-97', '+7-4-9-5-43-023-97', '4-3-0-2-3-9-7', 
              '8-495-430', '8(918) 523 84 95']

phone_book = list(map(clean, phone_book))
print(phone_book, type(phone_book))

shorts = filter(lambda x: len(x) == 7, phone_book)
start_w_8 = filter(lambda x: len(x) == 11, phone_book)
fulls = filter(lambda x: len(x) == 12, phone_book)
m1 = map(lambda x: '+7495' + x, shorts)
m1 = map(lambda x: '+7' + x[1], start_w_8)

phone_book = list(m1) + list(m2) + list (fulls)
print(phone_book, type(phone_book))

phone = phone_book.pop(0)
print(phone, type(phone))
print(phone_book, type(phone_book))

a1 = map(lambda x: phone == x, phone_book)

table = ['NO', 'YES']

a2 = map(lambda x: table[x], a1)
print(*a2, sep='\n')
