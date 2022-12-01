import sys
import queue

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_18258.txt')

n = int(sys.stdin.readline().rstrip())

q = queue.Queue()

for i in range(n):
    x, y = sys.stdin.readline().split()

    if x == "push":
        q.put(int(y))
    elif x == "pop":
        if q.empty() == True:
            print(-1)
        else:
            print(q.get()) 
    elif x == "size":
        print(q.full())
