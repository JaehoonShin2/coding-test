n, m = map(int, input().split())
x, y, d = map(int, input().split())

world = []
for i in range(n):
    world.append(list(map(int, input().split())))

def trun_left():
    global d
    if d == 0: d += 3
    else: d -= 1

def visit():
    global world
    world[x][y] = 2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시뮬레이션 시작
cnt = 1
turn_time = 0
while(True):
# 왼쪽으로 회전하기
    trun_left()
# 회전 후 이동하기
    nx = x + dx[d]
    ny = y + dy[d]
# 이동한 위치가 육지인지, 바다인지, 아니면 기존에 밟았던 곳인지 조건 검사
    if world[nx][ny] == 0 and world[nx][ny] != 2:
        x, y = nx, ny
# 새로이 방문한 육지의 좌표 값을 바탕으로 2로 변환
        visit()
# 움직인 숫자를 증가
        cnt += 1
        continue
# 왼쪽 방향에 가보지 않은 칸이 없다면 왼쪽 방향으로 회전만 수행
    else: turn_time += 1
# 만약 네 방향 모두 이미 가본 칸 or 바다로 되어 있는 칸    
    if turn_time == 4:
# 방향은 그대로 둔 채 한 칸 뒤로 이동
        nx = x - dx[d]
        ny = y - dy[d]
# 만약 뒤로 이동이 가능하다면
        if world[nx][ny] == 0:
            x, y = nx, ny
            visit()
        else : break
        turn_time = 0

print(cnt)





