import sys
from collections import deque

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_1697.txt')

n, k = map(int, sys.stdin.readline().split())

steps = [-1, 1, 2]
distance = [int(1e9)] * 100001

def bfs(v, target):
    q = deque()
    q.append(v)
    distance[v] = 0
    while q:
        now = q.popleft()
        if now == target:
            return distance[now]
        for step in range(3):
            if step == 2:
                node = now * steps[step]
            else :
                node = now + steps[step]

            if v < target : # 1, 1000
                if node > target+1 or 0 > node: continue
            if v > target : # 1000, 1
                if node > v or 0 > node:  continue

            if distance[node] > distance[now] and distance[node] == 1e9:
                distance[node] = min(distance[node], distance[now] + 1)
                q.append(node)
            else : continue


print(bfs(n, k))