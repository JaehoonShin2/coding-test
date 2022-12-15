import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_11066.txt')

t = int(sys.stdin.readline().rstrip())

for _ in range(t):

    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))

    #누적합을 담기 위한 리스트
    sum = [0 for _ in range(n+1)]

    for i in range(n):
        sum[i+1] = sum[i] + arr[i]
    
    dp = [[0 for i in range(n+1)] for _ in range(n+1)] #2차원리스트 선언

    # 2개 연속의 합, 3개 연속의 합.... n개 연속의 합, 즉 arr에 대한 총 갯수의 합
    for i in range(2, n+1):
        # 연속의 합을 구할 때 1~2, 2~3, 3~4, 1~3, 2~4, 1~4.. 와 같이 인덱스 값을 부여할 변수
        for j in range(1, n+2-i):
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (sum[j+i-1] - sum[j-1])   

    print(dp[1][n])

    

    # dp = [[0 for i in range(n+1)] for _ in range(n+1)]

    # sum = [0 for _ in range(n+1)]

    # for i in range(n):
    #     sum[i+1] = sum[i] + arr[i]
    
    # for i in range(2, n+1):
    #     for j in range(1, n+2-i):
    #         dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (sum[j+i-1] - sum[j-1])

    # print(dp[1][n])