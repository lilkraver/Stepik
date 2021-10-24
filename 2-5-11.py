ls = [int(i) for i in input().split()]
for i in set(ls):
    if ls.count(i) > 1:
        print(i, end=' ')
