import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_5597.txt')

data = []
for _ in range(28):
    data.append(int(sys.stdin.readline().rstrip()))

result = []
for i in range(1, 31):
    if i not in data:
        result.append(i)

result.sort()

for i in result:
    print(i)