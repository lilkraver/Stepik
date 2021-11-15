a, b, x, y = input(), input(), input(), input() 
puck, unpack = {}, {}               #словари для шифровки и дешифровки
for k in range(len(a)):         #для первой строки
    puck.update([(a[k], b[k])]) #добавл. данные словаря шифрования 
    unpack.update([(b[k], a[k])]) #добавл. данные словаря расшифровки
lst1 = []                  
for j in x:
    lst1.append(puck[j])   #пишем в список значения словаря шифрования 
print(''.join(lst1))
lst2 = [unpack[n] for n in y]  #пишем в список значения словаря расшифровки
print(''.join(lst2))
