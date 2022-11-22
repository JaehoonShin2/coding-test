array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)-1):
    #첫번째 인덱스의 값
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
print(array)
