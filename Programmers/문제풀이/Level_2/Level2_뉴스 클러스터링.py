import re, math
from collections import Counter, defaultdict

def solution(str1, str2):
    lower_1 = str1.lower()
    lower_2 = str2.lower()
    
    lower_1_list = [lower_1[x-1]+lower_1[x] for x in range(1, len(lower_1))]
    lower_2_list = [lower_2[x-1]+lower_2[x] for x in range(1, len(lower_2))]
    
    r = re.compile('[a-z][a-z]')
    
    regex_1 = [x for x in lower_1_list if r.match(x)]
    regex_2 = [x for x in lower_2_list if r.match(x)]
    
    if regex_1 == [] and regex_2 == []:
        return 65536
    else: 
        c_1 = Counter(regex_1)
        c_2 = Counter(regex_2)
        
        min_value = defaultdict(int)
        
        min_cnt = 0
        for k, v in c_1.items():
            if c_2[k] > 0:
                min_cnt += min(v, c_2[k])
                for _ in range(min(v, c_2[k])):
                    min_value[k] = min_value[k]+1
                    
        c_3 = c_1 + c_2
        
        for k, v in min_value.items():
            if c_3[k] > 0:
                c_3[k] -= min_value[k]
        
        max_cnt = sum(c_3.values()) 
        return math.floor(min_cnt/max_cnt*65536)

str1="aa1+aa2"
str2="AAAA12"
# str1="E=M*C^2"
# str2="e=m*c^2"
print(solution(str1, str2))