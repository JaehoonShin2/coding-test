import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_13305.txt')

n = int( sys.stdin.readline().rstrip())

arr1 = list(map(int, sys.stdin.readline().split()))

arr2 = list(map(int,sys.stdin.readline().split()))

result = 0

min = arr2[0]

result = arr1[0] * min

for i in range(1, n-1):
    if arr2[i-1] > arr2[i] and min > arr2[i]:
        min = arr2[i]
        result += min * arr1[i]
    else:
        result += min * arr1[i]

print(result)
    


