def solution(nums):
    return min(len(nums)/2, len(set(nums)))

nums=[3,3,3,2,2,4]
print(solution(nums))


# from collections import Counter
# def solution(nums):
    # counter = Counter(nums)
    # return len(counter) if len(counter) <= len(nums)/2 else len(nums)/2
