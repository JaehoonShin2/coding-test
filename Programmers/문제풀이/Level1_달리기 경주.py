def solution(players, callings):
    
    for called in callings:
        for idx, player in enumerate(players):
            if called == player:
                temp = players[idx-1]
                players[idx-1] = players[idx]
                players[idx] = temp
    
    
    answer = players
    return answer

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))