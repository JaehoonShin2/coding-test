from collections import Counter
def solution(nums):
    c = len(nums)/2
    counter = Counter(nums)
    max_c = len(counter)    
    if max_c <= c:
        return max_c
    else:
        return c

nums=[3,3,3,2,2,4]
print(solution(nums))