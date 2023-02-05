import sys

sys.stdin = open('/Users/s/Desktop/C/dev_study/coding-test/bj_2512.txt')

# 첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. 
# N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 
# N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 
# 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. 
# M은 N 이상 1,000,000,000 이하이다. 

n = int(sys.stdin.readline().rstrip())
nArr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())

nArr.sort()

def binary(start, end, target):
    
    while start <= end: 
        mid = (start + end) // 2
        if mid == target:
            print(mid)
            break
        elif mid < target:
            start = mid+1
        else:
            end = mid-1


if m >= sum(nArr) :
    print(max(nArr)) 
else :
    num = m // n
    for i in range(n):
        if num > nArr[i]:
            m -= nArr[i]
        else:
            r = m // (n-i)
            print(r)
            break
        
# 110 120 125 150 // 485//4
# 110 120 || 125 150
# 125 150 // (485-110-120)//2
# 125 || 150 
# 150 // (485-110-120-125)

def binary(arr, start, end, target):
    
    while start <= end:
        mid = (start + end) // 2
        m = target // n
        
        if arr[mid] <= m:
            for i in range(mid):
                m -= arr[i]
        else : 
            