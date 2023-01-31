import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_14002.txt")

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

            
print(max(dp))

arr = []
order = max(dp)
for i in reversed(range(n)):
    if dp[i] == order:
        arr.append(data[i])
        order -= 1

arr.reverse()
print(*arr)
