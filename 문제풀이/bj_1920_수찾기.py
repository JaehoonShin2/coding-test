import sys

# sys.stdin = open('C:/Users/R/Desktop/python_input/bj_1920.txt')

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
m = int(sys.stdin.readline().rstrip())
search = list(map(int, sys.stdin.readline().split()))

answer = []

def binory_search(arr, start, end, target):
    if start > end: 
        return None
    mid = (start + end) // 2
    if target == arr[mid]: 
        return 1
    elif target > arr[mid]:
        return binory_search(arr, mid+1, end, target)
    else:
        return binory_search(arr, start, mid-1, target)

for i in search:
    a = binory_search(arr, 0, n-1, i)
    if a == None: print(0)
    else: print(a)
