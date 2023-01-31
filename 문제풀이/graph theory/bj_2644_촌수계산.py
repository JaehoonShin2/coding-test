import sys
from collections import deque

sys.stdin = open('/Users/s/Desktop/C/dev_study/coding-test/python_input/bj_2644.txt')

# 사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 
# 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 
# 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 
# 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 
# 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.
# 각 사람의 부모는 최대 한 명만 주어진다.

# 1 초

n = int(sys.stdin.readline().rstrip())
start, target = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().rstrip())

graph = [ [] for i in range(n+1) ]
distance = [0] * (n+1)

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, target):
    q = deque()
    q.append(start)
    # 시작 노드를 deque 에 넣는다.
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            # 아직 방문 전이라면
            if distance[nxt] == 0:
                # 노드가 목표와
                if nxt == target:
                    return print(distance[cur] + 1)
                else :
                    distance[nxt] = distance[cur] + 1
                    q.append(nxt)
    return print(-1)


bfs(start, target)

          
          
          