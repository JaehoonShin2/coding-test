import sys

def binary(arr, t, s, e):
    if s > e: 
        return None
    mid = (s+e) // 2
    if arr[mid] == t: return mid
    elif t < arr[mid]:
        return binary(arr, t, s, mid-1)
    else:
        return binary(arr, t, mid+1, e)

n = int(sys.stdin.readline().rstrip())
item = list(map(int, sys.stdin.readline().split()))
item.sort()

m = int(sys.stdin.readline().rstrip())
order = list(map(int, sys.stdin.readline().split()))

for i in order:
    r = binary(item, i, 0, n-1)
    if r != None: print('yes', end=' ')
    else: print('no', end=' ')
