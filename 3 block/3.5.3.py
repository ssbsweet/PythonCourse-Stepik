import sys

x = ''
for i in range(1, len(sys.argv)):
    x += sys.argv[i] + ' '
print(x, end=' ')
