def solution(phone_book):
    dic = {}
    for i in phone_book:
        # 반복을 돌면서 map 에 key 값으로 전화번호 목록을 하나씩 입력
        dic[i] = 0
        
    for i in dic:
        # 맵에서 키(전화번호)를 하나씩 꺼내면서
        for j in range(1, len(i)):
            # 반복은 1부터 글자의 총길이-1 만큼만
            if (i[:j] in dic):
                # 슬라이싱 활용
                # 12[:1] => 1. 1이 맵의 키 중 하나에라도 존재하면 False
                # 123[:1] => 1. 123[:2] => 12... 12는 맵의 키 중에 존재하기 때문에 False 리턴
                return False
    return True
            

phone_book=["12","123","1235","567","88"]



print(solution(phone_book))

# def solution(phone_book):
    
#     for idx, phone in enumerate(phone_book):
#         for p in phone_book:
#             if phone != p:
#                 if phone == p[:len(phone)]:
#                     return False
#     return True

# def solution(phone_book):
    
#     phone_book = sorted(phone_book, key=lambda x: len(x))
#     print(phone_book)
#     for i in range(len(phone_book)-1):
#         for j in range(i+1, len(phone_book)):
#             if len(phone_book[i]) < len(phone_book[j]):
#                 if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                     return False