import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_14425.txt')

n, m = map(int, sys.stdin.readline().split())

dict = {}
for i in range(n):
    dict[i] = sys.stdin.readline().rstrip()

items = [sys.stdin.readline().rstrip() for _ in range(m)]

cnt = 0

for i in items:
    if i in dict.values():
        cnt +=1

print(cnt)