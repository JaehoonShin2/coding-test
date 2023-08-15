def solution():
    from sys import stdin
    
    N = int(stdin.readline().rstrip())
    order = []
    for _ in range(N):
        o = list(map(str, stdin.readline().rstrip().split(' ')))
        
        if o[0] == "push_front":
            order.insert(0, o[1])
        
        elif o[0] == "push_back":
            order.append(o[1])
        
        elif o[0] == "pop_front":
            print(order.pop(0)) if order else print(-1) 
        
        elif o[0] == "pop_back":
            print(order.pop()) if order else print(-1)
            
        elif o[0] == "size":
            print(len(order))
            
        elif o[0] == "empty":
            print(0) if order else print(1)
            
        elif o[0] == "front":
            print(order[0]) if order else print(-1)
            
        elif o[0] == "back":
            print(order[-1]) if order else print(-1)


if __name__ == "__main__":
    print(solution())