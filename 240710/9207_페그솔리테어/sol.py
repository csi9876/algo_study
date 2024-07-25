import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(k)]

# 1차원 dp
dp = [0] * (n + 1)

for v, t in arr:    # 과목 순회(가치, 공부시간)
    for j in range(n, t - 1, -1):   # 공부 시간 역순으로 순회
        #현재 과목 수강, 미수강 중 큰 가치 선택
        dp[j] = max(dp[j], dp[j - t] + v)

print(dp[n])