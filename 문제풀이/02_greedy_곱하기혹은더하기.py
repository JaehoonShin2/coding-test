import sys

str = sys.stdin.readline().rstrip()

cnt = len(str)
num = [0] * (cnt) 
for i in range(cnt):
    num[i] = int(str[i]) 

sum = num[0]

print(num)

for i in range(1, cnt):
    if num[i] <= 1 or sum <= 1:
        sum += num[i]
    else: sum *= num[i]

print(sum)