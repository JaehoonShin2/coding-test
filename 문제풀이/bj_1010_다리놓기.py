import sys
import math

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_1010.txt')

# def func(n):
#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    result = math.factorial(m) // (math.factorial(m-n) * math.factorial(n))
    print(result)

