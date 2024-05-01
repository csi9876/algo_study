import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# dp[i][j] : 1~i번째 색 중에서 j개의 색을 선택하는 경우의 수
dp = [[0]*(k+1) for _ in range(n+1)]


for i in range(n+1):
    for j in range(k+1):
        if j == 0:
            dp[i][0] = 1
            continue
        if j == 1:
            dp[i][1] = i
            continue

        if i == n:  # n번째 색을 선택하면 n-1과 1 번째 색을 선택하지 못함
            dp[i][j] = dp[i-1][j] + dp[i-3][j-1]
        else:       # i번째 색을 선택하면 i-1 번째 색을 선택하지 못함
            dp[i][j] = dp[i-1][j] + dp[i-2][j-1]
        dp[i][j] %= 1000000003

print(dp[n][k])