import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

T = int(input())
arr = list(map(int, input().split()))
N = int(input())

print(T, N, arr)

dp = [[0 for _ in range(T+1)] for _ in range(4)]

for i in range(len(arr)-(N-1)):
    for j in range(N):
        print(arr[i+j])
        dp[i] += arr[i+j]


print(dp)