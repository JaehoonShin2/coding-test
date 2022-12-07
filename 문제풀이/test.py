import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_14888.txt')

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

min_value = 1e9
max_value = -1e9


def dfs(cnt, arr):
#cnt = 데이터의 갯수
#arr = 데이터에서 연산이 완료된 뒤의 값

    global add, sub, mul, div, min_value, max_value

    if cnt == n:
        min_value = min(min_value, arr)
        max_value = max(max_value, arr)
        return
    else:
        if add > 0:
            add -= 1
            dfs(cnt+1, arr + data[cnt])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(cnt+1, arr - data[cnt])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(cnt+1, arr * data[cnt])
            mul += 1
        if div > 0:
            div -= 1
            dfs(cnt+1, int(arr / data[cnt]))
            div += 1

dfs(1, data[0])

print(min_value)
print(max_value)