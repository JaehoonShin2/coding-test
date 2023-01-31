import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_10816.txt')

n = int(sys.stdin.readline().rstrip())
arr = sorted( list(map(int, sys.stdin.readline().split())) )
m = int(sys.stdin.readline().rstrip())
search = list(map(int, sys.stdin.readline().split()))


def binory_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if target == arr[mid]:
        return cnt.get(target)
    elif target < arr[mid]:
        return binory_search(arr, target, start, mid-1)
    else:
        return binory_search(arr, target, mid+1, end)

cnt = {}
for i in arr:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in search:
    print(binory_search(arr, i, 0, n-1), end=' ')

