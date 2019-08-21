x = int(input())
if (x % 10 == 1) and (x % 100 != 11):
    print(x, 'программист')
elif (x % 10 == 2) and (x % 100 != 12) or (x % 10 == 3) and (x % 100 != 13) or (x % 10 == 4) and (x % 100 != 14):
    print(x, 'программиста')
else:
    print(x, 'программистов')
