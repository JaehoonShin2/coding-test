def solution(s, n):
    answer = ''
    for c in s:
        if c != ' ':
            i = ord(c)
            if i > 96 and i+n>122:
                i -= 26
            elif 90 >= i and i >= 65 and i + n > 90:
                i -= 26
            answer += chr(i+n)
        else:
            answer += " "
    return answer