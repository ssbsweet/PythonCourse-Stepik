x = []
summa = int(0)
square = int(0)
while (True):
    a = input()
    summa += int(a)
    if summa == 0:
        x.append(a)
        break
    x.append(a)
for i in range(len(x)):
    square += int(x[i]) ** 2
print(square)
