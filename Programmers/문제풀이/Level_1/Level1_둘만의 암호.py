def isCheck(node, skip_ord, index, cnt):
    # 만약 index 만큼 돌았다면 리턴
    if cnt == index:
        return node
    else:
        # node == 재귀에 넣은 문자 'a' 의 아스키코드값을 1 증가
        node += 1
        # 만약 z 보다 아스키코드 값이 커졌다면 a로 되돌려주기
        if node >= 123:
            node = node-123+97
        # 만약 node 가 스킵문자_아스키코드 리스트에 없다면
        if node not in skip_ord:
            # cnt 를 1 증가시킨 채 다음 재귀 호출
            return isCheck(node, skip_ord, index, cnt+1)
        else:
            # 스킵문자에 해당한다면 cnt 증가 없이 다시 재귀 호출
            return isCheck(node, skip_ord, index, cnt)

def solution(s, skip, index):
    answer = []
    # 스킵문자를 아스키코드로 치환
    skip_ord = [ord(x) for x in skip]
    for node in s:
        # 문자 하나당 아스키코드로 치환
        o = ord(node)
        # 재귀함수호출
        a = isCheck(o, skip_ord, index, 0)
        # 리턴받은 숫자를 다시 문자로 변환
        answer.append(chr(a))
    
    #하나의 문자열로 리턴
    return ''.join(answer)

    
s="aukks"
skip="wbqd"
index=5
s= "ybcde"
skip = "az"
index =1
#정답 : "bcdef"
print(solution(s, skip, index))