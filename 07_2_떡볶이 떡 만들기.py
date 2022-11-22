import sys
n, m = map(int, sys.stdin.readline().split())
tt = list(map(int, sys.stdin.readline().split()))
e = max(tt)

def binary(arr, t, s, e):
    if s > e: return None
    mid = (s+e)//2
    sum = 0
    for i in arr:
        result = i - mid
        if result >= 0: 
            sum += result
    if sum == t: return mid
    elif t < sum:
        return binary(arr, t, mid+1, e)
    else:
        return binary(arr, t, s, mid-1)

max = binary(tt, m, 0, e)
print(max)
