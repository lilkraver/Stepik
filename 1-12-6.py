n = int(input())
if(n % 100 == 11 or n % 100 == 12 or n % 100 == 13 or n % 100 == 14):
    print(n,'программистов')
elif(n == 1 or n % 10 == 1):
    print(n,'программист')
elif(n = =2 or n == 3 or n == 4 or n % 10 == 2 or n % 10 == 3 or n % 10 == 4):
    print(n,'программиста')
else:
    print(n,'программистов')
    
    
i = int(input())
d = i % 10
h = i % 100
if d == 1 and h != 11:
    s = ""
elif 1 < d < 5 and not 11 < h < 15:
    s = "а"
else:
    s = "ов"
print(i," программист" + s)
