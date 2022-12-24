import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/testInput.txt')

# 테스트케이스 횟수
t = int(sys.stdin.readline().rstrip())

# 장기의 움직임 
steps = [-1, 1]

# 최종 결과값
cnt = 0

def func(arr, x, visited):
    global cnt

    # 장기는 x를 기준으로 왼쪽 혹은 오른쪽으로 한 칸 이동
    for step in steps:
        nx = x + step
        
        # 만약 그래프를 벗어난다면 continue
        if nx < 0 or nx >= len(arr): continue
        # 만약 nx 인덱스의 값이 'Y' 이라면 continue
        if arr[nx] == 'Y': continue
        # 만약 한 칸 이동한 결과의 값이 'H' 이고, 아직 방문한 적이 없다면
        if arr[nx] == 'H' and visited[nx] == 0:
            # nx를 뛰어넘어, 즉 한 번 더 이동한 값을 nx에 저장
            nx += step
            # 방문처리
            visited[nx] = 1
            # 만약 한칸 더 이동한 인덱스가 범위 안에 있는지 확인
            if nx < 0 or nx >= len(arr): continue
            # x에서 2번 step을 한 결과가 'H' 라면 포를 잡을 수 잇다.
            if arr[nx] == 'H':
                # 방문처리
                visited[nx] = 1
                # 결과값 1 증가
                cnt += 1
                # 이동한 인덱스에서 다시 함수 호출
                func(arr, nx, visited)

for k in range(1, t+1):

    n = int(sys.stdin.readline().rstrip())

    graph = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]

    # x 노드의 좌표값을 받을 배열
    start = [0, 0]

    # 이중 for문을 통해 x의 좌표를 얻은 뒤 for문 종료
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                start[0] = i
                start[1] = j
                break
    
    # row 리스트에는 X의 x좌표를 기준으로 수평 데이터를 리스트에 입력
    row = graph[start[0]]
    # col 리스트에는 x의 y좌료를 기준으로 수직 데이터를 리스트에 입력
    col = []
    for i in graph:
        col.append(i[start[1]])

    # row1, col1 에는 각각 공백에 해당하는 L 을 제외한 리스트를 새로 입력
    row1 = []
    col1 = []

    for i in range(n):
        if 'L' != row[i]:
            row1.append(row[i])
        if 'L' != col[i]:
            col1.append(col[i])

    # row 와 col 의 방문 확인 여부를 입력하기 위한 리스트 선언
    visitedR = [0] * n
    visitedC = [0] * n

    # row1, col1 을 각각 func 함수 호출한 뒤 결과값을 anw 에 담기
    ans = []

    for i in range(len(row1)-1):
        if row1[i] == 'X':
            func(row1, i, visitedR)
            ans.append(cnt)
            break
    
    # col1를 사용한 함수 호출 전 다시 cnt 초기화
    cnt = 0

    for i in range(len(col1)-1):
        if col1[i] == 'X':
            func(col1, i, visitedC)
            ans.append(cnt)
            break
    
    s = "#" + str(k) + " "
    print(s+str(sum(ans)))

