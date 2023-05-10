from collections import deque, defaultdict

#철수는 최근 경제 상황이 좋지 않아 어쩔 수 없이 우범지역에 집을 구하게 되었다.
# 이 지역에는 N개의 교차로가 있고, N-1개의 길이 각각 두 교차로를 양방향으로 연결하고 있다.
# 교차로들은 1번부터 N번까지 번호가 붙어 있다. 어떤 교차로에서든 다른 교차로로
# 1개 이상의 길을 이용하여 이동할 수 있는 방법이 있다.

# 각 교차로에는 다세대 주택이 있는데, 그 다세대 주택의 집들 중에 범죄자가 살고 있을 수 있다.
# 철수는 어떤 교차로에 있는 다세대 주택에 범죄자가 있는지 여부를 모두 파악하였다.
# 아래 그림을 보면 8개의 교차로가 7개의 길로 연결되어 있다.
# 원 안의 숫자는 교차로의 번호이다.
# 원 옆에 있는 숫자는 해당 교차로에 범죄자가 살고 있는지 알려주는 것으로,
# 0 이면 범죄자가 살고 있지 않고, 1 이면 범죄자가 살고 있다는 뜻이다.

# 철수는 모든 교차로 i에 대해서 거리 K이내에 있는 교차로들 중 (교차로 i 포함) 범죄자가 살고 있는
# 교차로들의 개수를 계산하고 싶다. 교차로의 개수, 연결 상태와, 각 교차로에 범죄자가 사는지 여부를
# 입력 받아 그 답을 계산하는 프로그램을 작성하라. 편의상 출력은 모든 교차로에 대한 답을 더한 총 합으로 정한다.

# [입력]

# 입력 파일의 제일 첫째 줄에는 파일에 포함된 케이스의 수 T가 주어진다.
# 각 케이스의 첫째 줄에 교차로의 개수를 나타내는 자연수 N과 거리 K가 주어진다. (1 ≤ N ≤ 100,000, 0 ≤ K ≤ 100)
# 둘째 줄부터 N-1개의 줄에 걸쳐 도로들에 대한 정보가, 그 도로가 잇는 두 교차로의 번호로 주어진다.
# 어떤 교차로에서든 다른 교차로로 1개 이상의 길을 이용하여 이동할 수 있는 방법이 있다.
# 즉, 교차로들은 Tree 형태로 연결되어 있음에 유의하라. 다음 줄에 N개의 0 또는 1 값이 주어진다.
# 이 값들은 교차로의 번호 순서대로 각 교차로의 다세대 주택에 범죄자가 살고 있는지를 알려준다.
# 값이 0 인 경우 범죄자가 살고 있지 않은 교차로임을 의미하고, 값이 1 인 경우 범죄자가 살고 있는 교차로임을 의미한다.
 
# [출력]

# 각 테스트 케이스의 답을 순서대로 표준출력으로 출력하며, 각 케이스마다 줄의 시작에 “#x”를 출력하여야 한다.
# 이때 x는 케이스의 번호이다.
# 같은 줄에, 각 교차로에 대해 거리 K이내의 교차로들 중 범죄자가 살고 있는 교차로의 개수를 계산하여 모두 더한 총합을 출력한다.

def main():
    t = int(input())
    answers = []
    for _ in range(t):
        
        answer = 0
        
        N, K = map(int, input().split(' '))

        graph = defaultdict(list)
        
        for _ in range(N-1):
            x, y = map(str, input().split(' '))
            graph[x].append(y)
            graph[y].append(x)
        
        crime = list(map(int, input().split(' ')))
        
        for i in range(1, N+1):
            visited = [0] * (N+1)
            
            q = deque([(i, 0)])
            visited[i] = 1
            if crime[i-1] == 1:
                answer += 1
            
            while q:
                start, dist = q.popleft()
                for node in graph[str(start)]:
                    if dist == K:
                        continue
                    else:
                        # 방문 기록이 없고, 범죄가 1이라면 +1
                        if visited[int(node)] == 0:
                            q.append((node, dist+1))
                            visited[int(node)] = 1
                            
                            if crime[int(node)-1] == 1:
                                answer += 1
        answers.append(answer)           
    
    for idx, v in enumerate(answers):
        print('#'+str(idx+1)+str(v))

if __name__ == '__main__':
    main()