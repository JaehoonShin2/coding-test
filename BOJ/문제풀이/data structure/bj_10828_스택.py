import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_10828.txt')

t = int(sys.stdin.readline().rstrip())

orders = []
for i in range(t):
    orders.append(sys.stdin.readline().split())

ans = []
for o in orders:
    if o[0] == 'push':
        ans.append(o[1])
    elif o[0] == 'pop':
        if len(ans) == 0:
            print(-1)
        else: print(ans.pop())
    elif o[0] == 'size' :
        print(len(ans))
    elif o[0] == 'empty' :
        if len(ans) == 0:
            print(1)
        else: print(0)
    elif o[0] == 'top' :
        if len(ans) == 0:
            print(-1)
        else: print( ans[len(ans)-1])