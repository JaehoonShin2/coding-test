import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/testInput.txt')

t = int(sys.stdin.readline().rstrip())

steps = [-1, 1]

cnt = 0

def func(arr, x, visited):
    global cnt

    for step in steps:
        nx = x + step
        if nx < 0 or nx >= len(arr): continue
        if arr[nx] == 'Y': continue
        if arr[nx] == 'H' and visited[nx] == 0:
            nx += step
            visited[nx] = 1
            if nx < 0 or nx >= len(arr): continue
            if arr[nx] == 'H':
                visited[nx] = 1
                cnt += 1
                func(arr, nx, visited)

for k in range(1, t+1):

    n = int(sys.stdin.readline().rstrip())

    graph = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]

    start = [0, 0]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                start[0] = i
                start[1] = j

    row = graph[start[0]]
    col = []
    for i in graph:
        col.append(i[start[1]])

    row1 = []
    col1 = []

    for i in range(n):
        if 'L' != row[i]:
            row1.append(row[i])
        if 'L' != col[i]:
            col1.append(col[i])

    visitedR = [0] * n
    visitedC = [0] * n

    ans = []

    for i in range(len(row1)-1):
        if row1[i] == 'X':
            func(row1, i, visitedR)
            ans.append(cnt)
            break

    cnt = 0

    for i in range(len(col1)-1):
        if col1[i] == 'X':
            func(col1, i, visitedC)
            ans.append(cnt)
            break
    
    s = "#" + str(k) + " "
    print(s+str(sum(ans)))

