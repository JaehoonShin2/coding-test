import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('/Users/s/Desktop/C/dev_study/coding-test/python_input/bj_10815.txt')

# 2 초
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 
# -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 
# 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
# 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 
# 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고,
# 10,000,000보다 작거나 같다

# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 
# 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

n = int(sys.stdin.readline().rstrip())
nArr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
mArr = list(map(int, sys.stdin.readline().split()))

answers = []

nArr.sort()

def binary(arr, start, end, target):
    while start <= end:
        mid = ( start + end ) // 2   
        # 만약 배열의 중간 인덱스가 타겟과 동일하다면 바로 리턴
        if arr[mid] == target:
            return 1
        # 만약 배열의 중간 인덱스의 값보다 타겟이 작다면, binary(start, mid) 로 재귀
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return 0

for num in mArr:
    answers.append( binary(nArr, 0, n-1, num) )

print(*answers, end=' ')
