from collections import Counter
import re

def solution(s):

    num_dic = Counter(re.findall('\d+', s))
    answer = sorted(num_dic, key=lambda x:num_dic[x], reverse=True) 
    return list(map(int, answer))