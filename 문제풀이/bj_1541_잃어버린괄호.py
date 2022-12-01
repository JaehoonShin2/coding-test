import sys

#sys.stdin = open('C:/Users/R/Desktop/python_input/bj_1541.txt')

arr = sys.stdin.readline().split('-')

result = 0

for i in arr[0].split('+'):
    result += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
