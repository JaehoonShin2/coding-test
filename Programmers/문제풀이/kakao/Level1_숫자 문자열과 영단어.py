def solution(s):
    
    answer = s
    
    map = {"zero":'0',"one":'1', "two":'2', "three":'3', "four":'4',
           "five":'5', "six":'6', 'seven':'7', "eight":'8', "nine":'9'}
    
    for k, v in map.items():
        answer = answer.replace(k, v)
    
    return int(answer)

s="2three45sixseven"	
if __name__ == '__main__':
    print(solution(s))