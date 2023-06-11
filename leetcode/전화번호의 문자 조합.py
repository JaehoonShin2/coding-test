from itertools import product as p

def solution(digits):
    
    if digits == "": return []
    
    phone = {'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5':['j','k','l'],
             '6':['m','n','o'],
             '7':['p','q','r','s'],
             '8':['t','u','v'],
             '9':['w','x','y','z']}

    str_list = [phone[i] for i in digits]
    return [''.join(pr) for pr in list(p(*str_list))]

digits="23"
print(solution(digits))