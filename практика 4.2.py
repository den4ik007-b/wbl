import numpy as np


def clean(x):
    return ''.join(filter(lambda s: s not in {'-','(',')'},x))


phone_book = ['8(495)430-23-97', '+7-4-9-5-43-023-97', '4-3-0-2-3-9-7', 
              '8-495-430', '8(918) 523 84 95']

phone_book = np.vectorize(clean)(phone_book)
phone_book = np.vectorize(lambda x: x[-10:])(phone_book)
l = np.vectorize(len)(phone_book)
b7 = l == 7
phone_book[b7] = np.char.add('495', phone_book[b7])
table = ['NO', 'YES']
yes_no = map(lambda x: table[phone_book[0] == x], phone_book[1:])
print(*yes_no, sep='\n')
