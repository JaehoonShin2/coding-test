def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)

    for i in range( len(people)):
        
        if len(people)-1 == i:
                answer += 1
                print('4단계')
                print(people[i])
                break

        if limit - 40 < people[i]:
            answer += 1
            print('1단계')
            print(people[i])
        
        else:   
            # [-1] 인덱스가 없을 때..
            if  people[i] + people[-1] <= limit:
                answer += 1
                if len(people)-1 == i:
                    break
                people.pop(-1)
                print('2단계')
                print(people[i], people[-1])
            else:
                answer += 1
                print('3단계')
                print(people[i])
    
    return answer


def solution2(people, limit):
    
    answer = 0
    
    people.sort(reverse=True)

    start = 0 
    end = len(people) - 1
    
    while start < end :
        
        sum = people[start] + people[end]
  
        if sum > limit:
            start += 1
        
        else:
            start +=1
            end -= 1

        answer += 1

    if start == end:
        answer += 1

    return answer            
                
                
    


people = [70, 50, 80, 50]
people2 = [70, 80, 50]
limit = 100

print(solution2(people, limit))