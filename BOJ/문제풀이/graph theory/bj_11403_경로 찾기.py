import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_11403.txt')

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for row in graph:
    for col in row:
        print(col, end = " ")
    print()

