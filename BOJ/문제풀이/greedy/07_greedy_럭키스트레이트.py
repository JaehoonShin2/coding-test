import sys

n = sys.stdin.readline().rstrip()

half = len(n)//2

cnt0 = 0
cnt1 = 0

for i in range(len(n)):
    if i < half:
        cnt0 += int(n[i])
    else:
        cnt1 += int(n[i])

if cnt0 == cnt1:
    print("LUCKY")
else:
    print("READY")
