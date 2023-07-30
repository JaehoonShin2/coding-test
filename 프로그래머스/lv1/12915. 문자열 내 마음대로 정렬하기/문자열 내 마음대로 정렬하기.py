from collections import defaultdict as dd

def solution(strings, n):
    
    return sorted(sorted(strings), key=lambda x: x[n])