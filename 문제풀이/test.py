import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_14889.txt')

n = int(sys.stdin.readline().rstrip())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_value = 1e9
start = []
link = []

def dfs(idx):
    
    # 만약 스타트 팀의 인원이 전체 인원의 1/2 이 되었다면 링크 팀에 남은 인원을 넣은 뒤
    # 스타트 팀의 합과 링크 팀의 합을 각각 구한다.
    # 그 차이를 뺴준 뒤 절대값으로 바꿔주고, 그 값이 글로벌 변수인 min_sub 보다 작다면
    # 값을 바꾸어준다.

    if idx == n // 2:

        global min_value
        startSum = 0
        linkSum = 0

        # 각각의 팀에 모든 인원이 찼다.
        for i in range(n):
            if i not in start:
                link.append(i)
        
        #합을 구하기
        for i in range(n//2-1):

            for j in range(i+1, n//2):

                startSum += graph[ start[i] ][ start[j] ] + graph[ start[j] ][ start[i] ]
                linkSum += graph[ link[i] ][ link[j] ] + graph[ link[j] ][ link[i] ]
        
        diff = abs(startSum-linkSum)

        if(diff < min_value):
            min_value = diff
        
        link.clear()
        return

    # 아직 인원이 다 차지 않았다면
    else:
        for i in range(n):
            # start=[1,2]  i = 3
            # start의 갯수가 0개 이상이고, 스타트[ 2-1 ] > 3
            # 즉 스타트 리스트에 가장 마지막으로 담긴 값보다 i가 작다면 다름 for문
            if len(start) > 0 and start[len(start)-1] > i:
                continue
            if i not in start:
                start.append(i)
                dfs(idx + 1)
                start.pop()        

dfs(0)
print(min_value)