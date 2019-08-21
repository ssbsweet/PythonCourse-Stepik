import requests

with open('dataset_3378_3.txt') as inf:
    line = inf.readline().strip()

my_str = ''
while line.find('We') == -1:
    r = requests.get(line)
    my_str = r.text.splitlines()
    i = line.rfind('/')
    line = (line[0:i + 1] + my_str[0])

for s in my_str:
    print(s)
