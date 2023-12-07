import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(m) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = arr[i][j]
        elif i == 0 and j != 0:
            dp[i][j] = dp[i][j-1] + arr[i][j]
        elif j == 0 and i != 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        else:
            dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])