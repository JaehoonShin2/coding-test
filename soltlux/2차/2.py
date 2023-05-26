from collections import defaultdict as dd

def solution(n):
    
    aa = dd(int)
    bb = dd(int)
    cc = dd(int)
    
    aa['0'] = 1
    
    print(aa[0])

    
    a = [0]
    b = []
    c = []
    
    if n < 2:
        return 1
    for i in range(2, n+1):
        print('i의 값 : {}'.format(i))
        
        for j in range(i):
            if i - j == 2:
                print('zzzz : {}, {}'.format(aa[str(j)], bb[str(j)]))
                bb[str(j)] += aa[str(j)]
                print('bws : {}'.format(bb[str(j)]))
                aa[str(j)] = 0

        for k in range(i):
            print(i,k)
            print(i-k)
            print('ddd : {}, {}'.format(bb[str(k)], cc[str(k)]))
            if i-k == 4:
                cc[str(k)] += bb[str(k)]
                bb[str(j)] = 0
            else:
                aa[str(i)] += 1
        
    
    a_cnt = sum(x for x in aa.values())
    b_cnt = sum(x for x in bb.values())
    c_cnt = sum(x for x in cc.values())  
    
    return a_cnt+b_cnt+c_cnt

n=6
print(solution(n))




# import heapq

# def solution(n):
    
#     a = [0]
#     b = []
#     c = []
    
#     if n < 2:
#         return 1
    
#     for i in range(2, n+1):
#         print('i의 값 : {}'.format(i))
        
#         temp_a = -1
#         for j in range(len(a)):
#             print(i, a[j])
#             if i-a[j] == 2:
#                 heapq.heappush(b, i)
#                 temp_a = j
#             else:
#                 break
        
#         a = a[temp_a+1:]
        
#         print('a : {}'.format(a))
#         # b.sort()
#         # temp_b = -1
#         temp_b = b[:]
#         for k in range(len(b)):
#             if i-b[k] == 4:
#                 # temp_b = k
#                 heapq.heappop(temp_b)
#                 c.append(b[k])
#             else:
#                 a.append(i)
        
#         # b = b[temp_b+1:]   
#         b = temp_b
#         print('바뀐 a의 값 : {}'.format(a))      
#         print('바뀐 b의 값 : {}'.format(b))
#         print('바뀐 c의 값 : {}'.format(c))
        
#     return len(a) + len(b) + len(c)

# n=6
# print(solution(n))
