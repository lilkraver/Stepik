s = 0 #накоп перем для суммы
n = 0 #накоп перем для суммы квадратов
while True:
    k = int(input())
    s = s + k
    n = k ** 2 + n
    if s == 0:
        break
print(n)
