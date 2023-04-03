import sys
from queue import PriorityQueue

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_1927.txt')

n = int(sys.stdin.readline().rstrip())
arr = [ int(sys.stdin.readline().rstrip()) for _ in range(n) ]

q = PriorityQueue()
result = []

if arr[0] == 0:
    result.append(0)
else:
    q.put(arr[0])

for i in range(1, n):    
    if arr[i] != 0:
        q.put(arr[i])
    elif arr[i] == 0:
        if q.empty():
            result.append(0)
        else:
            result.append(q.get(arr[0]))

for i in result:
    print(i)

