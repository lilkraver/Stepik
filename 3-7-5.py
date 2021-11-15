d = {i:[0, 0] for i in range(1, 12)}
with open('dataset_3380_5.txt') as a:
    for i in a:
        s = i.split('\t')
        sum_height = d[int(s[0])][0] + int(s[2])
        n = d[int(s[0])][1] + 1
        d[int(s[0])] = [sum_height, n]
for i in d:
    if d[i][1] == 0:
        print(i, '-')
    else:
        print(i, d[i][0]/d[i][1])
        
     
    
d = dict()
with open('dataset.txt') as inf:
    for line in inf:
        a, b, c = line.strip().split( )
        d.setdefault(a, []).append(int(c))
k = 1 
while k <= 11:
    if str(k) in d.keys():
        print(k, sum(d.get(str(k)))/len(d.get(str(k))))
    else:
        print(k, '-')
    k += 1
