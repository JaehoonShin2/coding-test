import sys

# 1~n명의 사람들과 돈을 인출하는 데 걸리는 시간 Pn
n = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

result = []
sumNum = 0

for i in range(n):
    sumNum += arr[i]
    result.append(sumNum)
    
print(sum(result))
