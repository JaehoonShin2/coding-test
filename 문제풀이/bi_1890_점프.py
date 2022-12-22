import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_1890.txt")

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0

def func(x, y):
    global result

    if x == n-1 and y == n-1:
        result += 1
        return
    elif x >= n or y >= n:
        return
    else:
        num = graph[x][y]
        func(x+num, y)
        func(x, y+num)
        return

func(0, 0)
print(result)