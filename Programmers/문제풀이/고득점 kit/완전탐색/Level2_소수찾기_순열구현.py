permutation = []
answer = 0

def solution(numbers):
    for l in range(1, len(numbers)+1):
        latters = []
        dfs(l, latters)
        print(permutation)
    
    num_set = set()
    for p in permutation:
        s = ''
        for i in p:
            s += numbers[int(i)]
        num_set.add(int(s))
        
    for num in num_set:
        find(num)
        
    return answer    


def find(num):
    global answer
    
    if num > 1:
        print(num)
        for i in range(2, num+1):
            if i == num:
                answer += 1
            if num%i == 0:
                break
    else:
        return        
    


def dfs(l, latters):
        
    if len(latters) == l:
        permutation.append(''.join(map(str, latters)))
        return

    else:
        for node in range(len(numbers)):
            if node not in latters:
                latters.append(node)
                dfs(l, latters)
                latters.pop()


numbers = "011"
print(solution(numbers))

