input_data = input()
x = int(input_data[1])
y = ord(input_data[0]) - ord('a') + 1

result = 0

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

for i in range(len(dx)):
    nx = x + int(dx[i])
    ny = y + int(dy[i])
    if nx < 1 or nx > 8 or ny < 1 or ny > 8 : continue
    else : result += 1

print(result)

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

# for step in steps:
#     nx = x + int(step[0])
#     ny = y + int(step[1])
#     if nx < 1 or nx > 8 or ny < 1 or ny > 8 : continue
#     else : result += 1


# print(result)
