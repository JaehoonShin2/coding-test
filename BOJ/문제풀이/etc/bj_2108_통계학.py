import sys
from queue import PriorityQueue

sys.stdin = open('C:/Users/R/Desktop/python_input/bj_2108.txt')

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

n = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

print(round(sum(nums)/n))

nums.sort()
print(nums[int((n-1)/2)])


# 최빈값
counts = dict()
for i in range(1,n+1) :
	counts[i] = []

maxCount = 1
count = 1
for j in range(1,n) :
	if nums[j] == nums[j-1] :
		count += 1
	else :
		counts[count].append(nums[j-1])
		if maxCount < count: maxCount = count
		count = 1
	if j == n-1 : 
		counts[count].append(nums[j])
		if maxCount < count : maxCount = count

if n == 1 :
	counts[1].append(nums[0])

counts[maxCount].sort()
if len(counts[maxCount]) == 1 :
	print(counts[maxCount][0])
else :
	print(counts[maxCount][1])


print(nums[-1]-nums[0])



