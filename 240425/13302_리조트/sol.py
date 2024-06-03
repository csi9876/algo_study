import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

# 1일권 10000
# 3일권 25000, 1일권 1장
# 5일권 37000, 1일권 2장
# m일 제외 모든 날 리조트


n, m = map(int, input().split())
arr = list(map(float, input().split()))
inf = sys.maxsize

# 날짜, 쿠폰 dp
dp = [[inf]*106 for _ in range(106)]    # 최대 쿠폰 사용 개수는 40 + 3 * 20 = 106
dp[0][0] = 0

for i in range(n+1):    # 여행 일수
    for j in range(40):  # 최대 쿠폰 발행 갯수
        res = dp[i][j]
        if i+1 in arr:  # 할인 쿠폰 적용
            dp[i+1][j] = min(res, dp[i+1][j])
        if j >= 3:   # 3개 이상의 쿠폰
            dp[i+1][j-3] = min(res, dp[i+1][j-3])

        # 1일권
        dp[i + 1][j] = min(dp[i + 1][j], res + 10000)
        # 3일권
        for k in range(1, 4):
            if i + k <= n:
                dp[i + k][j + 1] = min(dp[i + k][j + 1], res + 25000)
        # 5일권
        for k in range(1, 6):
            if i + k <= n:
                dp[i + k][j + 2] = min(dp[i + k][j + 2], res + 37000)

print(min(dp[n]))