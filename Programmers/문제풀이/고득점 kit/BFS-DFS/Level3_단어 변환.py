from collections import deque

def solution(begin, target, words):
    
    # 타겟 단어가 words 에 없을 경우 0을 리턴한다.
    if target not in words:
        return 0
    
    # l 은 words 의 총 갯수
    l = len(words)
    # k 는 단어의 길이
    k = len(words[0])
    
    # 방문여부를 확인하는 리스트
    visited = [False] * l
    # deque
    q = deque()
    q.append((begin, 0))
    
    while q:
        print(q)
        word, dist = q.popleft()
        
        # 만약 현재 q의 word 와 target 이 동일하다면 dist 을 리넡
        if word == target:
            return dist
        
        # l(words) 만큼 반복을 돌아주면서 
        for i in range(l):
            # 방문한 기록이 없다면 
            if not visited[i]:
                diff_count = 0
                for j in range(k):
                    if word[j] != words[i][j]:
                        diff_count += 1
                
                if diff_count == 1:
                    visited[i] = True
                    q.append((words[i], dist + 1))
    
    return 0 

begin='hit'
target='cog'
words=["cog", "dot", "hot","dog", "lot", "log"]
print(solution(begin, target, words))