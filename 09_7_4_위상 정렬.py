import sys
from collections import deque

#노드의 갯수와 간선의 갯수를 입력
v, e = map(int, sys.stdin.readline().split())
#모든 노드에 대한 진입차수를 0으로 초기화
indegree = [0] * (v+1)
#간선 정보를 담을 graph 리스트 생성
graph = [[] for _ in range(v+1)]

#간선 정보를 입력받기. 그 과정에서 만약 a->c, b->c 와 같이 b의 값이 여러 개라는 것은
#진입차수가 복수 존재한다는 것임으로 indegree[b] 값을 증가시켜줌
for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

#위상 정렬 함수 생성
def topology_sort():
    result = [] #알고리즘 수행 결과를 담을 리스트
    q = deque() #큐 기능을 사용하기 위한 depue 라이브러리

    #가장 우선적으로 진입하게 될 q는 진입차수가 0인 노드 
    for i in range(1, v+1):
        if indegree[i] == 0: #만약 i노드의 진입차수가 0 이라면
            q.append(i) #q에 i노드를 넣는다.
    
    while q: #q가 텅빌 때까지 반복
        #큐에서 가장 앞에 있는 노드를 꺼낸다.
        now = q.popleft()
        #그 후 해당 노드를 결과값을 담을 result 리스트에 넣는다.
        result.append(now)

        #진입차수가 0인 첫 번째 노드가 정상적으로 결과 리스트에 담겼다면, 해당 노드에서 진입 가능한 노드들의 진입차수를 1 빼고,
        #그 다음 진입차수가 0인 노드를 찾아서 큐에 넣고 결과 리스트에 받는 과정을 반복한다.
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()

