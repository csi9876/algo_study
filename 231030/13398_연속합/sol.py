import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]
dp1[0] = arr[0]
dp2[0] = -999999999
result = -999999999
for i in range(1, n):
    dp1[i] = max(arr[i], arr[i]+dp1[i-1])
    dp2[i] = max(dp1[i-1], dp2[i-1]+arr[i])

for i in range(n):
    result = max(result, dp1[i], dp2[i])
print(result)