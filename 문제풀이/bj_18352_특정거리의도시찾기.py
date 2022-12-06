import sys
from collections import deque

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_18352.txt")

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def bfs(graph, start):
    q = deque([start])
    distance[start] = 0
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if distance[i] == -1: #방문하지 않은 노드면 추가 및 거리 갱신
                distance[i] = distance[now] + 1
                q.append(i)

bfs(graph, x)

if distance.count(k):
    for i in range(1,n+1):
        if distance[i] == k:
            print(i)
else:
    print("-1")