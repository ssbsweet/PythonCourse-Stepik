count_dict = int(input())
dict = []
check_words = []
result = []

for i in range(count_dict):
    dict.append(input().lower())

count_lines = int(input())

for i in range(count_lines):
    check_words += input().lower().strip().split(' ')

for i in check_words:
    if i not in dict and i not in result:
        result.append(i)

for i in result:
    print(i)
