n=int(input())
d={}
s=[]
for i in range(0,n):
    x=int(input())
    s.append(x)
for i in range(0,len(s)):
    key=s[i]
    if key in d:
        print(d[key])
    elif key not in d:
        z=s[i]
        d[key]=f(z)
        print(d.get(key))
