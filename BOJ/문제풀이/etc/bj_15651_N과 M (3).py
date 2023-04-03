import sys

n, m = map(int, sys.stdin.readline().split())

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    else:
        for i in range(1, n+1):
            s.append(i)
            dfs()
            s.pop()

dfs()

