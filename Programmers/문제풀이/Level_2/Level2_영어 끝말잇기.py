def solution(n, words):
    stack = []
    for k, v in enumerate(words):
        if not stack:
            stack.append(v)
        else:
            if v in stack:
                return [k%n + 1, k//n+1]      
            if stack[-1][-1] != v[0]:
                return [k%n + 1, k//n+1]              
            stack.append(v)        
    return [0, 0]    

n=5
words=["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
n=3
words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print(solution(n, words))