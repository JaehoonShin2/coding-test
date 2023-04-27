def solution(today, terms, privacies):
    answer = []
    
    t_dict = {}
    for term in terms:
        rate, month = term.split(' ')
        t_dict[rate] = month
    
    t_y, t_m, t_d = map(int, today.split('.'))
    
    for idx, privace in enumerate(privacies):
        date, currnet_rate = privace.split(' ')
        month = int(t_dict[currnet_rate])
        
        y, m, d = map(int, date.split('.'))
        
        # 시작 날짜가 2 이상
        # 만약 시작 날짜가 1이라면 m-1
        if d > 1:
            d -= 1
            if m+month < 13:
                m += month
            else:
                m = m+month
                y += m//12
                m %= 12
            
        else:
            d = 28
            month -= 1
            if m+month < 13:
                m += month
            else:
                m = m+month
                y += m//12
                m %= 12
        
        print('y, m, d : {}.{}.{}'.format(y,m,d))
        print('t_y, t_m, t_d : {}.{}.{}'.format(t_y, t_m, t_d))
        
        if t_y > y:
            answer.append(idx+1)
        elif t_y == y:
            if t_m > m:
                answer.append(idx+1)
            elif t_m == m:
                if t_d > d:
                    answer.append(idx+1)
            
    return answer


today="2022.05.19"
terms=["A 6", "B 12", "C 3"]
privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


print(solution(today, terms, privacies))