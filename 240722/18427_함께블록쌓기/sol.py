import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline


n, m, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n) ]

dp = [0] * (h+1)

for ar in arr:
    for idx in range(h, 0, -1):
        if not dp[idx]:
            continue

        for num in ar:
            if idx + num > h:
                continue
            dp[idx+num] += dp[idx]

    for num in ar:
        dp[num] += 1

print(dp[h]%10007)