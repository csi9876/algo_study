import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


# 1번돌에서 점프해서 n번 돌로 이동
# 처음 점프는 무조건 1>2로 1칸
# 가속/감속 점프 가능 = 이전에 x칸 점프면 x-1, x, x+1 칸 점프 가능
# 1칸 이상 점프해야함
# 작은 돌은 못 올라간다

n, m = map(int, input().split())
arr = list(int(input()) for _ in range(m))

# 최대 점프 거리를 계산
max_s = int((2*n)**0.5) + 1

dp = [[float('inf')] * (max_s+1) for _ in range(n+1)]

# 첫 시작
dp[1][0] = 0

# 2~n 번 돌
for stone in range(1, n+1):
    if stone in arr:
        continue

    for v in range(1, max_s):
        dp[stone][v] = min(dp[stone - v][v-1], dp[stone - v][v], dp[stone - v][v+1]) + 1

res = min(dp[n])
if res == float('inf'):
    print(-1)
else:
    print(res)