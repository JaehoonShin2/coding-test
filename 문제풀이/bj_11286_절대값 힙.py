import sys
from queue import PriorityQueue

#sys.stdin = open('C:/Users/R/Desktop/python_input/bj_11286.txt')

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

q = PriorityQueue()

for i in arr:
    if(i == 0):
        if(q.empty()):
            print(0)
        else:
            print(q.get()[1])
    else:
        #abs(i)를 기준으로 i를 우선순위 큐에 넣는다.
        q.put((abs(i), i))

