import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_14889.txt')

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
start = []
link = []


def dfs(idx):
    #최종적으로 반환하려는 값
    global min_value
    #백트래킹의 탈출조건
    if idx == n // 2 :
        startSum = 0
        linkSum = 0
        #0에서 n까지 반복을 돌면서 만약 i값이 start에 없다면 link 리스트에 담아준다.
        for i in range(0, n):
            if i not in start:
                link.append(i)
        
        for i in range(0, n//2 -1):
            for j in range(i, n//2):
                startSum += graph[  start[i]  ][  start[j]  ] + graph[ start[j] ] [ start[i] ]
                linkSum += graph[ link[i] ][ link[j] ] + graph[ link[j] ][ link[i] ]
        diff = abs(startSum - linkSum)
        if min_value > diff:
            min_value = diff
        # 링크 리스트는 항상 계산이 끝나면 비워줘야한다.
        link.clear()
        return
    else:
        for i in range(n):
            #한 번 들어온 데이터가 두 번 이상 들어오면 안되기 때문에 확인
            if i in start: 
                continue
            #만약 start 리스트의 데이터가 0이상이고, start 리스트에...?
            if len(start) > 0 and start[len(start)-1] > i:
                continue
            start.append(i)
            dfs(idx + 1)
            start.pop()

min_value = 1e9
dfs(0)
print(min_value)

