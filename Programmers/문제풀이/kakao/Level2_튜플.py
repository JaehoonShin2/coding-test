# 중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
# 원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
# 튜플의 원소 개수는 유한합니다.

from collections import Counter
import re

def solution(s):

    num_dic = Counter(re.findall('\d+', s))
    answer = sorted(num_dic, key=lambda x:num_dic[x], reverse=True) 
    return list(map(int, answer))


s="{{20,111},{111}}"
print(solution(s))