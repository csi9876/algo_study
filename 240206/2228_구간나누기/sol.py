import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

min_n = -sys.maxsize

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

# 3차원 dp
dp = [[[min_n for _ in range(2)] for _ in range(m + 1)] for _ in range(n + 1)]

# dp 배열 초기화
for i in range(n+1):
    for j in range(m+1):
        for k in range(2):
            if j == 0 and k == 0:
                dp[i][j][k] = 0
                continue
            dp[i][j][k] = min_n

# 최대합 구하기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(0, 2):
            # i번째 숫자를 구간에 포함하지 않음
            if k == 0:
                # i-1 번째 원소가 j번째 구간에 포함되었는지, 포함되지 않았는지 중요하지 않음(영향을 받지 않음)
                # i-1번째 선택까지의 합 중 큰 것을 선택
                dp[i][j][k] = max(dp[i - 1][j][0], dp[i - 1][j][1])

            # i번째 숫자를 구간에 포함
            elif k == 1:
                # i번째 숫자를 기존 구간에 포함시키는 경우의 수와 새로운 구간을 만든 경우의 수 중 큰 것을 고름
                dp[i][j][k] = max(dp[i - 1][j - 1][0], dp[i - 1][j][1]) + arr[i - 1]

# 최종 결과 출력
print(max(dp[n][m][0], dp[n][m][1]))