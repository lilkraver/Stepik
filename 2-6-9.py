lst, x = input().split(), input()
if x in lst:
    for i in range(len(lst)):
        if lst[i] == x:
            print(i, end=' ')
else:
    print('Отсутствует')
