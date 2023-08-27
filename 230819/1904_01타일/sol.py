import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N = int(input())
d = 15746
dp = [0] * (N+5)
dp[1] = 1
dp[2] = 2
dp[3] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-2]+dp[i-1]) % d
print(dp[N])
