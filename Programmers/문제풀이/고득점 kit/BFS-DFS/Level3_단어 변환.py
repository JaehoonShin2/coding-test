from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    l = len(words)
    k = len(words[0])
    
    visited = [False] * l
    q = deque()
    q.append((begin, 0))
    
    while q:
        word, dist = q.popleft()
        
        if word == target:
            return dist
        
        for i in range(l):
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