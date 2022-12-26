import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_9012.txt')

t = int(sys.stdin.readline().rstrip())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(t)]

for i in arr:
    cnt = 0
    for j in range(len(i)):
        if cnt < 0:
            break
        if i[j] == '(':
            cnt += 1
        if i[j] == ')':
            cnt -= 1
    if cnt == 0:
        print('YES')
    else : 
        print('NO')