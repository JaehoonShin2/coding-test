import sys
from collections import deque

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_1697.txt')

n, k = map(int, sys.stdin.readline().split())

distance = [0] * 100001

def bfs(v, target):
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        if x == target:
            print(distance[x])
            return
        for nx in ( x-1, x+1, x*2):
            if 0 <= nx < 100001 and distance[nx] == 0 :
                distance[nx] = distance[x] + 1
                q.append(nx)


bfs(100000, 1)