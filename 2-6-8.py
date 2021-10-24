k = int(input())
s = []
for i in range(1, k+1):
    s.extend([i] * i)
print(*s[:k])
