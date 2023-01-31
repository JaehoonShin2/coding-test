import sys

s = sys.stdin.readline().rstrip()

def solution(s):
    answer = int(1e9)
    
    for t in range(1, len(s)//2 + 2):
        #문자열 단위를 1부터 2, 3... s//2 +1(홀수 고려) 만큼 반복
        #만약 문자열의 길이가 1일 경우, len(1)//2 는 0이 되고, +1을 하여도 for 반복문 사용이 불가능해지기에
        # lne(s)//2 +2 .. 2를 더해준다.

        #새로운 문자열을 담을 문자열 객체
        ss = ''
        #문자열 단위의 반복 갯수
        cnt = 1
        #최초의 반복 문자열
        tmp = s[:t]
        
        for i in range(t, len(s)+t, t):
            
            if tmp == s[i:i+t]:
                cnt += 1
            else:
                if cnt > 1:
                    ss += str(cnt)
                ss += tmp
                tmp=s[i:i+t]
                cnt = 1
        print(ss)
        answer = min(answer, len(ss))

    return answer

print(solution(s))