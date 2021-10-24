a, b, c, d = (int(input()) for x in range(4))
for i in range(c, d + 1):
    print('\t' + str(i), end=' ')
print(end='\n')
for j in range(a, b + 1):
    print(str(j) + '\t', end=' ')
    for k in range(c, d + 1):
        print(str(j * k),end='\t')
    print(end='\n')  
