count = 0
queens = [0] * 15

# 유망한지 판단하는 함수
def promising(cdx) :
	# 같은 열이면 안되고, 대각선상에 있어서도 안 된다.
	for i in range(cdx):
		if (queens[cdx] == queens[i] or cdx - i == abs(queens[cdx] - queens[i])) :
			return 0
	return 1

# nqueen 알고리즘 수행
def nqueen(cdx, queens) :
    global count
	# cdx가 마지막 행까지 수행하고 여기까지 오면, 찾기 완료
	
    if (cdx == n) :
        count += 1
        return

    for i in range(n):
        queens[cdx] = i # cdx번째 행, i번째 열에 queen을 놓아본다.	
        # 이후 그 행에 둔 것에 대한 유망성을 판단한다.
        if (promising(cdx)) : #그 자리에 두어도 괜찮았다면,
            nqueen(cdx + 1, queens) # 그 다음 행에 대해 퀸을 놓는 것을 해 본다.

    

def solution(n):
    
    queens = []
    nqueen(0, queens)
    print(count)
    
n=4
print(solution(n))