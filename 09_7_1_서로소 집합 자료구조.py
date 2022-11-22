import sys

def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(p, x):
    if parent[x] != x:
        return find_parent(p, parent[x])
    return x

#노드의 갯수, 간선의 갯수
v, e = map(int, sys.stdin.readline().split())
#각 노드의 부모 노드를 나타내줄 리스트 생성
parent = [[] for _ in range(v+1)]

for i in range(v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합", end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print("각 노드의 부모 노드", end=' ')
for i in range(1, v+1):
    print(parent[i])
