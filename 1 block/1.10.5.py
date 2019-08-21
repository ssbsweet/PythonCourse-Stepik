A = int(input())  # минимум
B = int(input())  # максимум
H = int(input())  # факт
if A <= H <= B:
    print('Это нормально')
elif H >= B:
    print('Пересып')
else:
    print('Недосып')
