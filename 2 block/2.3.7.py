a = int(input())
b = int(input())
x = 0
middle = 0
for y in range(a, b + 1):
    if y % 3 == 0:
        x += 1
        middle += y
print(middle / x)
