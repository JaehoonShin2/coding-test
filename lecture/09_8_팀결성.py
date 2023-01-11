import sys


#중복..기법
def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]

def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    z, a, b = map(int, sys.stdin.readline().split())
    if z == 0:
        union_parent(parent, a, b)
    elif z == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

