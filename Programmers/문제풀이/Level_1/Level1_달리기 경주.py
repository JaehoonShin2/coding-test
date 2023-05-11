def solution1(players, callings):
    
    for called in callings:
        for idx, player in enumerate(players):
            if called == player:
                temp = players[idx-1]
                players[idx-1] = players[idx]
                players[idx] = temp
    
    
    answer = players
    return answer

def solution(players, callings):
    
    # 자료가 100만개 이기 때문에 시간복잡도 상 1번의 for 문으로 문제 해걸
    
    # dict 로 players의 idx 를 key로 잡고 value 로 player 를 담아볼까
    
    dict = {idx:v for idx, v in enumerate(players)}
    reversed_dict = {v:k for k, v in dict.items()}
    
    
    for called in callings:
        print('1단계')
        temp_idx = reversed_dict[called]
        temp_value = dict[temp_idx]
        print('추월한 사람의 idx, value : {}, {}'.format(temp_idx, temp_value))
        
        # 추월된 선수의 idx, value
        overtake_value = dict[temp_idx-1]
        overtake_idx = reversed_dict[overtake_value]
        print('추월당한 사람의 idx, value : {}, {}'.format(overtake_idx, overtake_value))

        # 추월된 사람의 idx 값에 called 값을 넣고
        dict[overtake_idx] = called
        reversed_dict[temp_value] = overtake_idx

        # 추월한 사람의(기존의) idx 값에 추월된 사람의 value=overtake_value 를 넣기.
        dict[temp_idx] = overtake_value
        reversed_dict[overtake_value] = temp_idx

    answer = []
    
    for v in dict.values():
        answer.append(v)
    
    return answer


players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))