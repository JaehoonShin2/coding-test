import sys
from queue import PriorityQueue

n = int(sys.stdin.readline().rstrip())

q = PriorityQueue()
result = []

for i in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if q.empty() == True:
            result.append(0)
        else:
            result.append( q.get()[1] )
    else:
        q.put((-x, x))

for i in result:
    print(i)