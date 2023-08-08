def solution(s):
    
    temp = ""
    answer = ""
    
    map = {"zero":0,"one":1, "two":2, "three":3, "four":4,
           "five":5, "six":6, 'seven':7, "eight":8, "nine":9}
    
    for c in s:
        if c.isnumeric():
            answer += c
        else:
            temp += c
            if map.get(temp) != None:
                answer += str(map[temp])
                temp = ""
    
    return int(answer)