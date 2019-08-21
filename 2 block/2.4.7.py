inp = str(input())
a = 1
b = 1
res = inp[b:b + 1]
for x in inp:
    if x in res:
        a += 1
    else:
        print(x, end='')
        print(a, end='')
        a = 1
    b += 1
    res = inp[b:b + 1]
