import sys

#노드간 연결되지 않은 것을 나타내줄 임의의 값
INF = int(1e9)
#노드의 갯수와 간선의 갯수
n, m = map(int, sys.stdin.readline().split())
#시작노드값 지정
start = int(sys.stdin.readline().rstrip())
#각 노드의 정보를 담을 수 있는 그래프를 생성(그래프는 n+1로 생성)
graph = [[] for i in range(n+1)]
#노드의 방문여부를 나타낼 리스트
visited = [False] * (n+1)
#노드의 이동거리를 표시할 리스트
distance = [INF] * (n+1)

#노드간 연결 여부를 입력받는 2차원 리스트를 그래프에 입력
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

#최단거리 여부를 확인하고 방문처리하는 함수
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1): #반복은 노드1의 거리부터 노드n(인덱스상으로는 n+1)만큼
        # 만약 i인덱스(i노드)의 거리의 값이 inf보다 작고, 아직 방문 전이라면
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

#다익스트라 함수 생성
def dijkstra(start):
    #시작노드의 거리값은 0
    distance[start] = 0
    #시작노드의 방문여부를 true로 수정
    visited[start] = True
    #시작노드에서부터 뻗어갈 수 있는 노드에 대한 거리를 표시
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작노드를 뺀 n-1개의 노드만큼 반복을 돌면서 각 노드의 연결여부 및 최단거리를 확인하는 반복문 실행
    for i in range(n-1):
        # 각 노드부터의 최단 거리 여부를 확인해주는 함수 실행
        now = get_smallest_node()
        #now == index 값이자 i번째 인덱스에서 출발해서 방문한 노드의 인덱스
        visited[now] = True
        #now노드부터 다시 시작해서 뻣어나갈 수 있는 다른 노드들을 확인
        for j in graph[now]:
            #now 노드에 도착하기까지 걸린 최소 간선값 + now 노드에서 출발하는 간선값
            cost = distance[now] + j[1]
            # cost 와, 기존에 저장된 거리값을 비교
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

#1번노드부터 n+1, 즉 마지막 노드까지의 distance값을 출력
for i in range(1, n+1):
    if distance[i] == INF: print("INFINITY")
    else : print(distance[i])



            


