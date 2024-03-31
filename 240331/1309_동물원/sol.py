import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


## 2*n 칸 우리
## 사자 배치, 가로 세로 붙어있게 배치 X

n = int(input())

dp = [0] * (n+1)
dp[1] = 3

if n > 1:
    dp[2] = 7
    # dp[3] = 17  ## 2*7 + 3
    for i in range(3, n+1):
        dp[i] = (2*dp[i-1] + dp[i-2]) % 9901

print(dp[n])
