import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = [[0, 0]]
dp = [0]*(n+1)

for i in range(1, n):
    # 점프 저장
    a, b = map(int, input().split())
    arr.append([a, b])

k = int(input())

# 2번돌
if n >= 2:
    dp[2] = arr[1][0]

# 3번돌
if n >= 3:
    dp[3] = min(arr[1][1], dp[2] + arr[2][0])

# 최소값
res = int(1e9)

# 4~n돌까지 에너지 계산
if n >= 4:
    for i in range(4, n+1):  # 매우 큰 점프를 할 수 있는 위치
        for j in range(4, n+1):  # 큰 점프를 할 수 있는 돌의 위치
            # 매우 큰 점프로 돌에 도달
            if i == j:
                dp[j] = dp[j - 3] + k
            else:
                dp[j] = int(1e9)
            # 작은 점프와 큰 점프로 돌에 도달
            dp[j] = min(dp[j], min(dp[j - 2] + arr[j - 2][1], dp[j - 1] + arr[j - 1][0]))
        #  최소값 저장
        res = min(res, dp[n])
else:
    res = dp[n]

print(res)
