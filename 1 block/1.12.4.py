x = input()
if x == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    d = ((a + b + c) / 2)
    e = (d * ((d - a) * (d - b) * (d - c)))
    s = e ** 0.5
    print(s)
elif x == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif x == 'круг':
    r = float(input())
    y = r ** 2
    print(3.14 * y)

