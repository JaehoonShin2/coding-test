import sys

k = int(sys.stdin.readline().rstrip())

stack = []

for i in range(k):
    x = int(sys.stdin.readline().rstrip())
    if x != 0:
        stack.append(x)
    else:
        stack.pop()

print(sum(stack))