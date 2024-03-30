import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][1] = arr[0][0]
    dp[1][1] = arr[1][0]

    for i in range(2, n+1):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i-1]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i-1]
    print(max(dp[0][n], dp[1][n]))

