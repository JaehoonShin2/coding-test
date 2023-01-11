import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    line = sys.stdin.readline().split()
    name = line[0]
    point = int(line[1])
    arr.append((name, point))

arr.sort(key=lambda student: student[1])

for student in arr:
    print(student[0], end=' ')