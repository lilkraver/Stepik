form = str(input())
if(form == 'треугольник'):
    a = int(input())
    b = int(input())
    c = int(input())
    p = ((a + b + c)/2)
    s = (((p*(p - a)*(p - b)*(p - c)))** 0.5)
    print(float(s))
elif(form == 'прямоугольник'):
    a = int(input())
    b = int(input())
    print(float(a * b))
elif(form == 'круг'):
    r = int(input())
    print(float((r ** 2) * 3.14))
