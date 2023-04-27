def solution(lottos, win_nums):
    
    cnt = 0
    zero_cnt = lottos.count(0)
    rank=[6,6,5,4,3,2,1]
    
    for win_num in win_nums:
        if win_num in lottos:
            cnt += 1
    return [rank[cnt+zero_cnt], rank[cnt]]

def solution1(lottos, win_nums):
    min_num = len(set(lottos) & set(win_nums))
    max_num = min_num + lottos.count(0)
    answer = [max_num, min_num]
    answer = [7-x if x > 0 else 6 for x in answer]
    
    return answer


lottos=[44, 1, 0, 0, 31, 25]	
win_nums=[31, 10, 45, 1, 6, 19]
# lottos=[0, 0, 0, 0, 0, 0]
# win_nums=[38, 19, 20, 40, 15, 25]
# lottos=[45, 4, 35, 20, 3, 9]
# win_nums=[20, 9, 3, 45, 4, 35]
print(solution1(lottos, win_nums))