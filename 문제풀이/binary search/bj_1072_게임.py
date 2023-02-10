import sys

sys.stdin = open('/Users/s/Desktop/C/dev_study/coding-test/python_input/bj_1072.txt')

x, y = map(int, sys.stdin.readline().split())
z = ( y * 100 )// x

if z >= 99:
    print(-1)
else:
    ans = 0
    start = 1
    end = x

    while start <= end:
        mid = (start + end ) // 2
        if z < ( y + mid ) * 100 // (x + mid):
            ans = mid
            end = mid-1
        else:
            start = mid+1
            
    print(ans)