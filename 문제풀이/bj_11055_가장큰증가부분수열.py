import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_11055.txt')

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n+1) # 각 인덱스 위치에 가장 큰 증가 부분 수열의 합
dp[0] = m[0]

for i in range(1, n+1):
    for j in range(i):

        if m[i] > m[j]:
            dp[i] = max(dp[i], dp[j] + m[i])
        else:
            dp[i] = max(dp[i], m[i])

print(dp)