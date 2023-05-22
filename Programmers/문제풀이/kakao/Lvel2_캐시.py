from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    
    cities = [x.lower() for x in cities]
    q = deque()
    for idx, city in enumerate(cities):
        if not q:
            q.append(city)
            answer += 5
        else:
            if city not in q:
                answer += 5
                if len(q) < cacheSize:
                    q.append(city)
                else:
                    q.popleft()
                    q.append(city)
            else:
                answer += 1
                q.remove(city)
                q.append(city)
            
    
    return answer

cacheSize=2	
cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cacheSize=5
cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(cacheSize, cities))