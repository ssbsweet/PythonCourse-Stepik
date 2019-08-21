chislo = int(input())
x = 1
y = 1
z = 0
w = 0
while x <= chislo:
    y = 1
    z += 1
    while y <= z:
        if w == chislo:
            break
        print(z, end=' ')
        w += 1
        y += 1
    x += 1
