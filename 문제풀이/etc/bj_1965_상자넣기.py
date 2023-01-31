import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_1965.txt")

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

# 시간 제한 2초
# o(n) -> 2억 개
# o(n^2) -> 2만 개

# input 데이터 갯수 : 1000개 -> 2차원 for문 까지 가능

dp = [1] * (n)

# 가장 외부 상자, 즉 dp 상자에 해당나는 i
for i in range(1, n):
    
    # data[1] 부터 시작해서 외부상자 i 의 1개 전까지 반복하며
    # i에 들어갈 수 있는지 없는지는 확인하는 반복문

    for j in range(i):

        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
