def ascii(list):
    ord_list = []
    for l in list:
        ord_list.append(ord(l))
    return ord_list

def de_ascii(list):
    de_ascii_list = []
    for i in list:
        de_ascii_list.append(chr(i))
    return de_ascii_list
    
def solution(encrypted_text, key, rotation):
    
    ord_en = ascii(encrypted_text)
    
    if rotation < 0:
        for _ in range(abs(rotation)):
            a = ord_en.pop()
            ord_en.insert(0, a)
    else:
        for _ in range(rotation):
            a = ord_en.pop(0)
            ord_en.append(a)  
            
    ord_key = ascii(key)
    kk = [x-96 for x in ord_key]
    en = [ x-y for x, y in zip(ord_en, kk)]
    en = [ x if x > 96 else x+123-97 for x in en ]
    
    return ''.join(de_ascii(en))
    
encrypted_text='qyyigoptvfb'
key='abcdefghijk'
rotation=3

print(solution(encrypted_text, key, rotation))