import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for i in range(n + 2)]

dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, n + 2):
    dp[i] = dp[i - 1] + 1
    for j in range(i - 3, -1, -1):
        dp[i] = max(dp[i], dp[j] * (i - j - 1))

print(dp[n])