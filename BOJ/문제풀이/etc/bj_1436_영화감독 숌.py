import sys

n = int(sys.stdin.readline().rstrip())

d = [0] * (n+1)
index = 1
num = 666
while(True):
    if(d[n] != 0):
        print(d[n])
        break
    elif ('666' in str(num)):
        d[index] = num
        index += 1
    num += 1