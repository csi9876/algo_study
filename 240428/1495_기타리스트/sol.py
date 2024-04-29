import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

# n = 곡의 갯수,  s = 시작 볼륨,  m = 최대 볼륨
n, s, m = map(int, input().split())
# i번째 음악 볼륨 변경 : 현재 볼륨 + arr[i] or - arr[i]
arr = list(map(int, input().split()))

# 2차원으로 각 곡마다 가능한 볼륨
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            min_n = j - arr[i]
            max_n = j + arr[i]

            # 다음 곡에 현재 볼륨 담기
            if min_n >= 0:
                dp[i+1][min_n] = 1

            if max_n <= m:
                dp[i+1][max_n] = 1


res = -1
# m ~ 0까지 역순으로 확인
for i in range(m, -1, -1):
    # n번째 곡에서 가장 큰 볼륨
    if dp[n][i] == 1:
        res = i
        break
print(res)