
def solution(phone_book):

    d = dict()
    for idx, phone in enumerate(phone_book):
        list = []
            

    
        

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