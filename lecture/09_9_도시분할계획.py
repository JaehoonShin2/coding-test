import sys

def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]

def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a<b: p[b] = a
    else: p[a] = b

n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

edges = []

for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()

#최소신장트리의 결과값을 담는 변수
result = 0
last = 0

#cost를 기준으로 정렬이 완료된 graph 리스트를 가지고,
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)