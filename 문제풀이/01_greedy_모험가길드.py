import sys

n = int(sys.stdin.readline().rstrip())
people = list(map(int, sys.stdin.readline().split()))
people.sort()

cnt = 0
group = 0

for i in range(n):
    cnt += 1
    if cnt >= people[i]:
        group += 1
        cnt = 0

print(group)
