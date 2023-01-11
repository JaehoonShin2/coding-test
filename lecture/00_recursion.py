def hanoi(frm, to, n):
    if n == 1:
        print(f'{frm} {to}')
    else:
        empty = 6 - frm - to
        hanoi(frm, empty, n - 1)
        print(f'{frm} {to}')
        hanoi(empty, to, n - 1)


print('원반의 개수: ')
numberOfDisk = int(input())
print('원반들의 시작 위치: ')
startLocation = int(input())
print('옮겨야 할 위치: ')
desLocation = int(input())
print('\n')

hanoi(startLocation, desLocation, numberOfDisk)