phone_book = ['8(495)430-23-97', '+7-4-9-5-43-023-97', '4-3-0-2-3-9-7', 
              '8-495-430', '8(918) 523 84 95']

print(phone_book, type(phone_book))
print(phone_book[0], type(phone_book[0]))

phone_book = [x.replace('-', '').replace('(', '').replace(')', '')
              for x in phone_book]

for i in range(len(phone_book)):
    if len(phone_book[i]) == 7:
        phone_book[i] = '+7495' + phone_book[i]
    elif len(phone_book[i]) == 11:
        phone_book[i]= phone_book[i].replace('8', '+7', 1)
    
print(phone_book, type(phone_book))


for i in range(1, len(phone_book)):
    if phone_book[0] == phone_book[i]:
        print('YES')
    else:
        print('NO')