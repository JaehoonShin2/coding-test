import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_2805.txt')

m, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def binory_search(arr:list, target:int):
    start = 1
    end = max(arr)

    while start <= end:
        mid = (start+end)//2
        length = 0
        for i in arr: 
            if i > mid:
                length += i-mid
        if length < target:
            end = mid - 1
        elif length >= target:
            start = mid + 1
    return end

print(binory_search(arr, k))
