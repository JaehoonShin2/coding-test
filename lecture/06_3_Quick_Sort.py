arr=[5,7,9,0,3,1,6,2,4,8]

def qs(arr, start, end):
    if start>end: 
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        #왼쪽에서부터 피봇보다 크면서도 마지막 인덱스에는 접촉하지 않는 left 값을 찾는다
        while left <= end and arr[left] <= arr[pivot]: 
            left += 1
        #오른쪽에서부터 피봇보다 작으면서도 최초의 인덱스보다는 큰 right 값을 찾는다.
        while right > start and arr[right] >= arr[pivot]: 
            right -= 1
        #만약 left가 right보다 크다면, 즉 역전되었다면
        if left>right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        #그게 아니고 각각 피봇보다 큰 값과 작은 값을 찾았다면
        else:
            arr[left], arr[right] = arr[right], arr[left]
    #그렇게 해서 1차적인 피봇에 대한 정렬이 종료되었다면 분할정복법을 사용
    qs(arr, start, right-1)
    qs(arr, right+1, end)

qs(arr, 0, len(arr)-1)
print(arr)

    
