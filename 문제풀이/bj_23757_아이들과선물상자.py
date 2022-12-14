import sys
from queue import PriorityQueue

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_23757.txt')

n, m = map(int, sys.stdin.readline().split())

q = PriorityQueue()
for i in list(map(int, sys.stdin.readline().split())):
    q.put( ((i*-1), i) )

q2 = PriorityQueue()
arr = list(map(int, sys.stdin.readline().split()))

result = True

for i in arr:
    x = q.get()[1]
    if(x < i):
        result = False
        break
    else:
        q.put( ((i-x),x-i))


if(result):
    print(1)
else:
    print(0)


