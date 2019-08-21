a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
n = (((p - a) * (p - b) * (p - c)) * p) ** 0.5
print(n)
