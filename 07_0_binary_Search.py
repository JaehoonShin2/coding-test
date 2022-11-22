import sys

def binary_seacrch(arr, target, start, end):
    if start > end: return None
    mid = (start+end)//2
    if target == arr[mid]: return mid
    elif target < arr[mid]:
        return binary_seacrch(arr, target, start, mid-1)
    else:
        return binary_seacrch(arr, target, mid+1, end)
    

n, target = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = binary_seacrch(arr, target, 0, n-1)
if result == None: print("찾으시는 원소가 존재하지 않습니다.")
else: print(result+1)


