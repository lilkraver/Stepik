k = [0,0]
for i in range(int(input())):
    a=[str(i) for i in input().split()]
    if a[0] == 'север':
        k[1] += int(a[1])
    if a[0] == 'восток':
        k[0] += int(a[1])
    if a[0] == 'юг':
        k[1] -= int(a[1])
    if a[0] == 'запад':
        k[0] -= int(a[1])
print(k[0], k[1], sep=' ')



dict = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}
for _ in range(int(input())):
    key, value = input().split()
    dict[key] += int(value)
print(dict['восток'] - dict['запад'], dict['север'] - dict['юг'])
