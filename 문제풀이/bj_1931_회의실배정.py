import sys

n = int(sys.stdin.readline().rstrip())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arr.sort(key=lambda x:(x[1], x[0]))
# key=lambda x: (정렬하고하 하는 기준 설정)
# x[1] arr의 1인덱스 기준으로 정렬 후 
# x[0], 0인덱스로 한번 더 정렬

cnt = 0
curEnd = 0
for start, end in arr:
    if curEnd <= start:
        curEnd = end
        cnt += 1

print(cnt)