import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
# e = arr.pop()
dp = [[0] * 21 for _ in range(N)]

# print(dp)
# print(dp[0])
dp[0][arr[0]] = 1
# print(dp[0])
# print(dp)

for i in range(1, N-1):
    for j in range(0, 21):
        if dp[i-1][j] != 0:
            xx = j - arr[i]
            yy = j + arr[i]

            if i == N-2:
                if 0 <= xx <= 20 and xx == arr[-1]:
                    dp[i][xx] += dp[i - 1][j]
                if 0 <= yy <= 20 and yy == arr[-1]:
                    dp[i][yy] += dp[i - 1][j]
            else:
                if 0 <= xx <= 20:
                    dp[i][xx] += dp[i-1][j]
                if 0 <= yy <= 20:
                    dp[i][yy] += dp[i-1][j]

# print(dp[N-1])
res = dp[N-2]
print(res[arr[-1]])
