a, b = int(input()), int(input())
d = a * b
while(a != 0 and b != 0):
    if(a > b):
        a = a % b
    else:
        b = b % a
print(int(d / (a + b)))
