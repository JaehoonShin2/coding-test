import sys

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_23027.txt')

input = sys.stdin.readline().rstrip()

def func(input):
    chars = 'ABC'
    changeChars = 'BCDF'

    for i in range(len(chars)):
        if chars[i] in input:
            for j in range(i, len(changeChars)):
                input = input.replace(changeChars[j], chars[i])
            print(input)
            return

    if('A', 'B', 'C' not in input):
        print('A' * len(input))
        return


func(input)