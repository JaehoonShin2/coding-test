import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_10830.txt')

n, b = map(int, sys.stdin.readline().split())

graph = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]


## 행렬 x와 y를 제곱하는 함수
def func(x, y):
    l = len(x) # 행렬 길이
    temp = [[0]*(l) for _ in range(n)]

    for row in range(l):
        for col in range(l):
            #반복문을 돌때마다 초기화
            z = 0
            for i in range(l):
                z += x[row][i] * y[i][col]
            temp[row][col] = z % 1000

    return temp

def div(graph, b):
    if b == 1:
        for x in range(len(graph)):
            for y in range(len(graph)):
                graph[x][y] %= 1000
        return graph
    
    tmp = div(graph, b//2)
    if b % 2:
        return func(func(tmp,tmp), graph)
    else:
        return func(tmp, tmp)

result = div(graph, b)
for r in result:
    print(*r)