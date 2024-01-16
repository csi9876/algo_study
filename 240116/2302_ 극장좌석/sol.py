import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
arr = [int(input()) for _ in range(m)]

dp = [0] * (n+1)
dp[0] = 1
if n >= 1:
    dp[1] = 1
if n >= 2:
    dp[2] = 2

# 점화식
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

ans = 1     # 경우의 수
if m > 0:   # 고정석 있으면
    temp = 0    # 부분

    for i in range(m):
        ans *= dp[arr[i] - 1 - temp]    # 부분집합
        temp = arr[i]   # 이전 숫자
    ans *= dp[n - temp]     # 곱하기
else:
    ans = dp[n]

print(ans)




'''
123 4 56 7 89
123 65
123 65 98
123 98

213
213 65
213 98
213 65 98

132
132 65
132 98
132 65 98
'''