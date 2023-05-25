def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        idx = 0
        valid = True
        
        for s in st:
            if s in skill:
                if s != skill[idx]:
                    valid = False
                    break
                idx += 1
                
        if valid:
            answer += 1
        
    return answer

skill="CBD"	
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]
skill = "CBD"
skill_trees = ["CEAZIDNLK"]
print(solution(skill, skill_trees))