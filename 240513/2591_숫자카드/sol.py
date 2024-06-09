import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = list(map(int, input().strip()))
dp = [[0 for _ in range(35)] for _ in range(len(n))]
dp[0][n[0]] = 1

for i in range(1, len(n)):
    for j in range(1, 35):
        temp = 10 * j + n[i]
        if temp <= 34:
            dp[i][temp] += dp[i-1][j]
        dp[i][n[i]] += dp[i-1][j]

print(sum(dp[-1][1:]))