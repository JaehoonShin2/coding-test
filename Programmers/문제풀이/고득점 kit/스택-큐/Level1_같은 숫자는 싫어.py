def solution(arr):
    return [arr[i] for i in range(len(arr)) if arr[i:i+1] != arr[i+1:i+2]]
    

arr=[1,1,3,3,0,1,1]
print(solution(arr))


# def solution(arr):
    # answer = [arr[0]]
    # for i in range(1, len(arr)):
    #     if arr[i-1] != arr[i]:
    #         answer.append(arr[i])