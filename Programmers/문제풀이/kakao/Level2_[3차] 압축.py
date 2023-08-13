def solution(msg):
    
    # 영문 대문자와 색인 번호를 매칭
    dic = dict(zip([chr(c) for c in range(ord('A'), ord('Z')+1)] ,range(1, 27)))
    
    answer = []
    
    m = list(msg)
    # 색인을 위한 문자. 초기값은 0번째 문자
    temp = m.pop(0)
    # 색인이 성공했을 때의 해당 문자열의 색인값을 담을 변수
    temp_idx = 0
    # 색인이 안되는 문자열을 추가할 때의 사용할 색인 번호
    max_idx = 26

    # temp, 즉 문자가 없을 때까지 반복
    while temp != "":
        # 문자가 색인 사전에 있다면
        if temp in dic:
            # 또한 아직 msg 리스트가 존재한다면
            if m:
                temp_idx = dic[temp]
                # msg 리스트에서 가장 앞 문자를 temp에 추가
                temp += m.pop(0)
            # 만약 더이상 msg 문자열이 존재하지 않는다면 가장 마지막 문자이기 때문에 리턴
            else:
                answer.append(dic[temp])
                return answer
        # temp 문자가 색인 사전에 없다면, 색인사전에 등록하고 가장 마지막 문자를 temp에 대입
        else:
            answer.append(temp_idx)
            max_idx += 1
            dic[temp] = max_idx
            temp = temp[-1]

    return answer

# LZW(Lempel–Ziv–Welch) 압축
# 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 단계 2로 돌아간다.


msg="KAKAO"
msg="TOBEORNOTTOBEORTOBEORNOT"

if __name__ == "__main__":
    print(solution(msg))