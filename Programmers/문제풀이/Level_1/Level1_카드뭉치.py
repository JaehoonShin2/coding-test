def solution(cards1, cards2, goal):
    
    ans = ['Yes', 'No']
    
    for s in goal:
        if len(cards1) > 0 and s == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and s == cards2[0]:
            cards2.pop(0)
        else:
            return ans[1]
    return ans[0]
    
    
cards1=["i", "drink", "water"]
cards2=["want", "to"]
goal=["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal))