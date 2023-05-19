def gcd(n, m):
    return m if n % m == 0 else gcd(m, n%m)

def solution(w,h):
    c, d = max(w, h), min(w, h)
    return (w*h)-(w+h-gcd(c, d))

w, h = 8, 12
print(solution(w, h))