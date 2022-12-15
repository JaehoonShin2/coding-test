import sys

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_11651.txt")

n = int(sys.stdin.readline().rstrip())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

nums.sort(key=lambda x : (x[1], x[0]))

for (x, y) in nums:
    print(x, y)