n = int(input())
x, y = 1, 1
plans = input().split()

# x좌표와 y좌표로 이동하게 되는 경우의 수 나열
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range( len(move_types) ):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # nx외 ny로 임시 이동 값을 저장한 뒤 조건문을 통해 경로를 벗어났는지 검사
    if nx < 1 or nx > n or ny < 1 or ny > n :
        continue
    x, y = nx, ny

print(x, y)

