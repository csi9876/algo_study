import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    t, p = map(int, input().split())
    arr.append([t,p])
dp = [0] * (N+1)
temp = 0
for i in range(N):
    temp = max(temp, dp[i])
    if i+arr[i][0] > N:
        continue
    dp[i+arr[i][0]] = max(temp+arr[i][1], dp[i+arr[i][0]])
print(max(dp))