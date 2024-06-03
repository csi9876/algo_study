import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


t, w = map(int, input().split())
arr = [0]
for i in range(t):
    a = int(input())
    arr.append(a)

dp = [[0 for _ in range(w+1)] for _ in range(t+1)]

for i in range(1, t+1):
    if arr[i] == 1:     # 1번에 서있으니 1에 떨어지면 + 1
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, w+1):
        # 1번에 서있고 짝수 이동, 2번에 서있고 홀수 이동이면
        # +1
        if (arr[i] == 1 and j % 2 == 0) or (arr[i] == 2 and j % 2 != 0):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[t]))
