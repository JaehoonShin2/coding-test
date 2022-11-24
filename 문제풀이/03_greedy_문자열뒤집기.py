import sys

s = sys.stdin.readline().rstrip()
cnt0 = 0
cnt1 = 0


if s[0] == '1':
    cnt0 += 1 #첫번째 원소가 1일 경우 0으로 바꾸는 경우의 수에 +1
else:
    cnt1 += 1 #첫번째 원소가 0일 경우 1로 바꾸는 경우의 수에 +1

#두번째 원소부터 0인지 1인지 확인하고 바꾸는 경우의 수에서 더해주기
for i in range( 1, len(s) ):
    if s[i-1] != s[i]:        
        if s[i] == '1':
            cnt0 += 1 #i-1번째 원소가 i번째 원소가 다르고, i번째 원소가 1일 경우 0으로 바꾸는 경우의 수에 +1
        else:
            cnt1 += 1 #i-1번째 원소가 i번째 원소가 다르고, i번째 원소가 0일 경우 1로 바꾸는 경우의 수에 +1

print(min(cnt0, cnt1))


