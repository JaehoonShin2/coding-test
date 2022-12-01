import sys

# sys.stdin = open('C:/Users/R/Desktop/python_input/bj_1654.txt')

n, k = map(int, sys.stdin.readline().split())
arr = [ int(sys.stdin.readline().rstrip()) for _ in range(n) ]

def binory_search(arr, target):
    start = 1
    end = max(arr)
    while start <= end:
        mid = (start+end)//2
        cable_cnt = [ (i // mid) for i in arr ]
        if sum(cable_cnt) < target:
            end = mid-1
        elif sum(cable_cnt) >= target:
            start = mid+1
    
    return end

print(binory_search(arr, k))