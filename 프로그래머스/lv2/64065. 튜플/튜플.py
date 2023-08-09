from collections import defaultdict as dd
import re

def solution(s):
    
    num_dic = dd(int)
    
    split_s = s.split('{')

    sss = [ss.split(',') for ss in split_s if ss != '']
     
    for sssss in sss:
        for sssssss in sssss:
            if sssssss != '':
                aa = re.sub('[^0-9]', '', sssssss)
                num_dic[aa] += 1    

    answer = sorted(num_dic, key=lambda x:num_dic[x], reverse=True)
    
    return list(map(int, answer))