import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_10816.txt')

n = int(sys.stdin.readline().rstrip())
arr = sorted( list(map(int, sys.stdin.readline().split())) )
m = int(sys.stdin.readline().rstrip())
search = list(map(int, sys.stdin.readline().split()))


cnt = {} # dictionary를 사용하기
for i in arr:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in search:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')