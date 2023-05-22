import math

def lcm(a,b):
  return (a * b) // math.gcd(a,b)

def solution(arr):
    answer = 1
    for node in arr:
        answer = lcm(answer, node)
    
    return answer

arr=[1,2,3]	
print(solution(arr))