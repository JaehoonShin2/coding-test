import sys

n = sys.stdin.readline().rstrip()
list = list(map(int, sys.stdin.readline().split()))
list.sort()

target = 1

for i in list:
    if target < i:
        break
    target += i
    

print(target)

