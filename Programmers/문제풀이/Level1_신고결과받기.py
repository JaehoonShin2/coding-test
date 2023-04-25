from collections import Counter

def solution(id_list, report, k):
    answer = []
    
    # 중복 제거
    report = list(set(report))
    
    # 신고당한 사람을 담을 리스트
    report_cnt = []
    
    # 신고한 사람과 신고 당한 사람을 담을 딕셔너리
    report_dict = {id: set() for id in id_list}
    
    for node in report:
        a, b = node.split(' ')
        # 리스트에 신고당한 사람을 추가
        report_cnt.append(b)
        # 딕셔너리에 key 로 신고한 사람에 대해서 누굴 신고했는지를 담음
        report_dict[a].add(b)
            
        # print('신고자 : {}, 피신고자 : {}'.format(a, b))
    
    # 신고당한 사람과 그 중복숫자를 딕셔너리로 바꿔주는 라이브러리
    report_cnt = Counter(report_cnt)
    
    print(report_dict)
    print(report_cnt)
    
    # for key, value in report_cnt.items():
    #     if value >= k:
    #         print('k회 이상 신고 당한 사람 : {}'.format(key))
    #         for key in report_dict:
    #             print(key)
    for i in id_list:
        # 메일 받을 갯수
        result = 0
        for u in report_dict[i]:
            if report_cnt[u] >= k:
                result += 1
        answer.append(result)
    
    # print(report_dict)
    return answer


# id_list=["muzi", "frodo", "apeach", "neo"]	
# report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	
# k=2

id_list=["con", "ryan"]
report=["ryan con", "ryan con", "ryan con", "ryan con"]
k=3

print(solution(id_list, report, k))