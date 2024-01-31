import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input().strip())
MOD = 1000000
dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

# 1일 출석, 지각, 결석 1회 경우 체크
dp[1][0][0], dp[1][0][1], dp[1][1][0] = 1, 1, 1


'''
DP[N][0][0] = ~n일 지각 0 연속 결석 0
DP[N][0][1] = ~n일 지각 0 연속 결석 1
DP[N][0][2] = ~n일 지각 0 연속 결석 2
DP[N][1][0] = ~n일 지각 1 연속 결석 0
DP[N][1][1] = ~n일 지각 1 연속 결석 1
DP[N][1][2] = ~n일 지각 1 연속 결석 2
'''

for N in range(1, n):
    dp[N+1][0][0] = (dp[N][0][0] + dp[N][0][1] + dp[N][0][2]) % MOD
    dp[N+1][0][1] = dp[N][0][0]
    dp[N+1][0][2] = dp[N][0][1]
    dp[N+1][1][0] = (dp[N][1][0] + dp[N][1][1] + dp[N][1][2] + dp[N][0][0] + dp[N][0][1] + dp[N][0][2]) % MOD
    dp[N+1][1][1] = dp[N][1][0]
    dp[N+1][1][2] = dp[N][1][1]


print((dp[n][1][0] + dp[n][1][1] + dp[n][1][2] + dp[n][0][0] + dp[n][0][1] + dp[n][0][2]) % MOD)