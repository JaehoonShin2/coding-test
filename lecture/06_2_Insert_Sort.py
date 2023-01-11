array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)-1):

    for j in reversed(range(i)):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
        else: break

print(array)