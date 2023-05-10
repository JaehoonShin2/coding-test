from collections import deque, defaultdict
from sys import stdin

# N개의 교차로가 있고, N-1개의 길이 각각 두 교차로를 양방향으로 연결하
def main():
    t = int(stdin.readline())
    a = []
    for _ in range(t):
        
        answer = 0
        
        N, K = map(int, stdin.readline().split(' '))
        print('N : {}, K : {}'.format(N, K))

        graph = defaultdict(list)
        
        for _ in range(N-1):
            x, y = map(str, stdin.readline().rstrip().split(' '))
            print('x : {}, y : {}'.format(x, y))
            graph[x].append(y)
            graph[y].append(x)
        
        crime = list(map(int, stdin.readline().rstrip().split(' ')))
        print('crime : {}'.format(crime))
        
        for i in range(1, N+1):
            visited = [0] * (N+1)
            
            q = deque([(i, 0)])
            visited[i] = 1
            if crime[i-1] == 1:
                answer += 1
            
            while q:
                # 시작점
                start, dist = q.popleft()
                
                start = str(start)
                
                for node in graph[start]:
                    
                    if dist == K:
                        continue
                    else:

                        # 방문 기록이 없고, 범죄가 1이라면 +1
                        if visited[int(node)] == 0:
                            q.append((node, dist+1))
                            visited[int(node)] = 1
                            
                            if crime[int(node)-1] == 1:
                                answer += 1
        a.append(answer)           
    
    for idx, aa in enumerate(a):
        print('#'+str(idx+1)+' '+str(aa))

if __name__ == '__main__':
    main()