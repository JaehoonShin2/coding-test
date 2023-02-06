import sys

sys.stdin = open('/Users/s/Desktop/C/dev_study/coding-test/bj_2512.txt')

# 첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. 
# N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 
# N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 
# 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. 
# M은 N 이상 1,000,000,000 이하이다. 

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())

start, end = 0, max(arr)

if m >= sum(arr):
    print(max(arr))
else:
    while start <= end:  # 이분탐색
        mid = (start + end) // 2  # 상한액 설정
        curr = 0
        for i in arr:
            if i >= mid:  # 요청한 금액이 상한액 이상이라면
                curr += mid  # 상한액 더하기
            else:  # 상한액 미만이라면
                curr += i  # 요청한 금액 더하기
        if curr <= m:  # 예산 총액이 총 예산 이하라면
            start = mid + 1
        else:  # 예산 총액이 총 예산을 초과한다면
            end = mid - 1

    print(end)