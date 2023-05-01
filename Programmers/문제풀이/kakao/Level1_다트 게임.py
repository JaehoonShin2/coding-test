from collections import deque

def solution(dartResult):
    answer = []
    n1 = ""

    for j in dartResult:
        n1 += j

        # 문자열인지 확인하는 함수
        if j.isalpha():
            answer.append(n1[:-1])
            answer.append(j)
            n1 = ""
            print('isalpha : {}'.format(answer))
        if j == "*" or j == "#":
            answer.append(j)
            n1 = ""

    q = deque(answer)
    cnt = []
    for y in range(len(q)):
        n2 = q.popleft()

        if n2 == "S" and cnt:
            cnt[-1] = int(cnt[-1])**1
        elif n2 == "D" and cnt:
            cnt[-1] = int(cnt[-1])**2
        elif n2 == "T" and cnt:
            cnt[-1] = int(cnt[-1])**3
        else:
            cnt.append(n2)

    # * 이나 # 이 없으면 그냥 모두 더해서 리턴.
    if "*" not in cnt and "#" not in cnt:
        return sum(cnt)

    final = []

    for j in cnt:
        if j == "#" and final:
            final[-1] = final[-1]*(-1)
            print(final)
            continue
        if j == "*" and final:
            if len(final) == 1:
                final[-1] = final[-1]*2
            if len(final) >= 2:
                final[-1] = final[-1]*2
                final[-2] = final[-2]*2

            continue

        final.append(j)
    return sum(final)




# dartResult="1D#2S*3S"
dartResult="1T2D3D#"
print(solution(dartResult))