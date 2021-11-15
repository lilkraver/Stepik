c = open('dataset_3363_2.txt', 'r').readline()
res = ''
a = ''
d = 0
for i in code:
    if i.isalpha():
        res += a * d
        a = i
        d = 0
    if i.isdigit():
        d = int(str(d) + i)       
res += a * d
print(res) 
