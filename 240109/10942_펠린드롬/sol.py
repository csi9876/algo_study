import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
q = [list(map(int, input().split())) for _ in range(m)]
dp = [[0] * n for _ in range(n)]


# 길이가 1인 경우
for i in range(n):
	dp[i][i] = 1

# 길이가 2인 경우
for i in range(n-1):
	if arr[i] == arr[i+1]:
		dp[i][i+1] = 1

# 길이 3 이상
for lens in range(2, n):
	for s in range(n - lens):
		e = s + lens

		if arr[s] == arr[e]:
			if dp[s + 1][e - 1] == 1:
				dp[s][e] = 1

for x, y in q:
	print(dp[x - 1][y - 1])