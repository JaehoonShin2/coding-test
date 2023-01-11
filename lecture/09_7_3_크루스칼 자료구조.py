import sys

#최소신장트리 알고리즘

#부모노드를 찾는 함수
#1) 중복압축기법 사용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
#2)일반적인 부모 노드 찾기 
def finds_parent(parent, x):
    if parent[x] != x:
        return finds_parent(parent, parent[x])
    return x

#union 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 갯수와 간선의 갯수. 그리고 부모노드에 대한 리스트
v, e = map(int, sys.stdin.readline().split())
parent = [[] for _ in range(v+1)]

#인접 리스트에 대한 정보를 담을 리스트
edges = []
#최소신장트리의 총합
result = 0

#최초에 각 노드의 부모 노드는 자기자신의 값으로 초기화
for i in range(1, v+1):
    parent[i] = i

for i in range(v+1):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append( (cost, a, b) )

#cost, 간선의 크기를 기준으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    #사이클, 즉 부모노드가 같은지 아닌지 확인. 만약 같아면 사이클.
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)