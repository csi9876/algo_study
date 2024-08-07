import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 누적합 배열 초기화
dp = [[0] * (n+1) for _ in range(n+1)]

# 누적합 계산
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 구간 합 계산
    res = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(res)