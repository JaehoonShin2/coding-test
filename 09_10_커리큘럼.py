import sys
from collections import deque
import copy

v = int(sys.stdin.readline().rstrip())
#모든 노드에 대한 진입차수 리스트를 담을 indegree 리스트를 선언 및 0으로 초기화
indegree = [0] * (v+1)
#각 노드에 대한 간선 정보를 담기 위한 graph 인접 리스트 초기화
graph = [[] for _ in range(v+1)]
#모든 강의에 대한 시간 데이터를 담을 리스트를 초기화
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, sys.stdin.readline().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    #q를 선언
    q = deque()
    
    #첫번째 q에는 진입차수가 0인 값을 넣는다.
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        #큐에서 원소를 꺼낸다.
        now = q.popleft()
        #꺼낸 원소에서 진입하게 되는 다음 원소들을 찾는다.
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            #이어지는 원소를 찾고, 진입차수를 1 제거하여 다음 진입차수가 0인 노드를 찾는다.
            if indegree[i] == 0:
                q.append(i)
    
    #반복문이 종료된 뒤, 위상정렬된 값을 출력하는 반복문 실행
    for i in range(1, v+1):
        print(result[i])

topology_sort()

