import numpy as np

def clean(x):
    return ''.join(filter(lambda s: s not in {'-','(',')'},x))



phone_book = ['8(495)430-23-97', '+7-4-9-5-43-023-97', '4-3-0-2-3-9-7', 
              '8-495-430', '8(918) 523 84 95']

print(phone_book, type(phone_book))
#ph_n = np.array(list(map(clean,phone_book)))


ph_n = np.fromiter(map(clean,phone_book),(str,12))
print(ph_n, type(ph_n))


l = np.fromiter(map(len, ph_n), int)

print(l, type(l))

ph_n[l == 7] = np.char.add('+7495', ph_n[1 == 7])
work = ph_n[l==11]

print(work)

work = np.fromiter(map(lambda x: x.replace('8', '+7', 1), work))

print(ph_n, type(ph_n))

#print(ph_n[len(ph_n) == 7])

#print(p,p[:10], p[-10:])

