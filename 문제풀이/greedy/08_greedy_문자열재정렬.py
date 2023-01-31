import sys

s = sys.stdin.readline().rstrip()

ss = []
n = 0

for i in range(len(s)):
    if ord(s[i]) > 64:
        ss.append(s[i])
    else:
        n += int(s[i])

ss.sort()

result = ""

for i in ss:
    result += i

print(result+str(n))
