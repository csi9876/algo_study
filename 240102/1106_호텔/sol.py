import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


c, n = map(int, input().split())
arr = []
max_ratio = 0
for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))



dp = [int(1e9)] * (c + 100)
dp[0] = 0   # 0원 투자했을 때 증가하는 고객 수

for i in range(0, n):
    x, y = arr[i]

    for j in range(y, c+100):
        # 고객을 늘리는 데 필요한 최소비용 + 추가 비용, 현재까지 계산된 j명 늘리는 최소 비용 중 최소값
        dp[j] = min(dp[j-y] + x, dp[j])

# c명 이상 최소비용 계산
print(min(dp[c:]))