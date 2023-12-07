import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

# 점화식
# dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
# 현재 계단 수 의 갯수는 전 단계의 끝자리가 -1, +1 인 경우의 합

N = int(input())
dp = [[0]*12 for _ in range(N+1)]
# 12인 이유는 0, 9는 전 단계가 1개라서 2개로 만들어주기 위함
dp[1][2:11] = [1]*9

for i in range(2, N+1):
    for j in range(1, 11):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)