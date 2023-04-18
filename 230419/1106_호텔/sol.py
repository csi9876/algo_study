import sys
sys.stdin = open('input.txt')

C, N = map(int, input().split())
arr = [(0,0)]
for _ in range(N):
    w, v = map(int, input().split())
    arr.append((w, v))
# print(arr)
dp = [int(1e9)]*(C+100)
dp[0] = 0
for i in range(1, N+1):
    w, v = arr[i]
    for j in range(v, C+100):
        dp[j] = min(dp[j-v] + w, dp[j])

print(min(dp[C:]))