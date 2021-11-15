all = open('dataset.txt', 'r')
s = all.read().lower().strip().split()
y = 0
m =''
for i in s:
    z = s.count(i)
    if z >= y:
        y = z
        m = i
print(m, y)
