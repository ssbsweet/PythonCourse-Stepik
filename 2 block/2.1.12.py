a = int(input())
b = int(input())
c = 1
while (c % a != 0) or (c % b != 0):
    c = c + 1
print(c)
