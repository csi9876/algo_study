import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = []
max_d = 0
for _ in range(n):
    p, d = map(int, input().split())
    arr.append((p, d))
    if max_d < d:
        max_d = d

dp = [0] * (max_d + 1)
# 큰 금액, 빠른 강연일 순으로 정렬
arr.sort(key=lambda x: (-x[0], x[1]))

for i in range(n):
    np, nd = arr[i][0], arr[i][1]
    # 큰 값을 주는 순서로 마감일부터 가까운 날로 오면서 확인
    for j in range(nd, 0, -1):
        if dp[j] == 0:
            dp[j] = np
            break

print(sum(dp))

