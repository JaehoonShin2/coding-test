import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_14888.txt')

n = int(sys.stdin.readline().rstrip())
#n개의 숫자
data = list(map(int, sys.stdin.readline().split()))
#연산자의 갯수
add, sub, mul, div = map(int, sys.stdin.readline().split())

min_value = 1e9
max_value = -1e9

def dfs(cnt, arr):
    global add, sub, mul, div, min_value, max_value
    #모든 수열을 다 받게 되었을 경우 최댓값과 최솟값 반환
    if cnt == n:
        min_value = min(min_value, arr)
        max_value = max(max_value, arr)
    #아직 수열의 계산이 덜 끝났을 경우
    else:
        if add > 0:
            add -= 1
            dfs(cnt+1, arr+data[cnt])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(cnt+1, arr-data[cnt])
            sub +=1
        if mul > 0:
            mul -= 1
            dfs(cnt+1, arr*data[cnt])
            mul += 1
        if div > 0:
            div -= 1
            dfs(cnt+1, int(arr/data[cnt]) )    
            div += 1


dfs(1, data[0])

print(max_value)
print(min_value)