# least common multiple
def lcm(n, m):
    return (n*m)//gcd(n,m)

# greatest common divisor
def gcd(n, m):
    return m if n%m == 0 else gcd(m, n%m)

def solution(n, m):
    c, d = max(n, m), min(n, m)
    return [gcd(c, d), lcm(c, d)]

n, m = 2, 5
print(solution(n, m))