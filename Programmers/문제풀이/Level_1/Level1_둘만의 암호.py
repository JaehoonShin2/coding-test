def isCheck(node, skip_ord, index, cnt):
    
    if cnt == index:
        return node
    else:
        node += 1
        if node >= 123:
            node = node-123+97
        if node not in skip_ord:
            return isCheck(node, skip_ord, index, cnt+1)
        else:
            return isCheck(node, skip_ord, index, cnt)


def solution(s, skip, index):
    answer = []
    skip_ord = [ord(x) for x in skip]
    for node in s:
        o = ord(node)
        a = isCheck(o, skip_ord, index, 0)
        answer.append(chr(a))
    
    return ''.join(answer)

    
s="aukks"
skip="wbqd"
index=5
s= "ybcde"
skip = "az"
index =1
#정답 : "bcdef"
print(solution(s, skip, index))