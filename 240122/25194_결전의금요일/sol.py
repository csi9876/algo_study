import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0]*7
dp[0] = 1

for i in arr:
    temp = [0] * 7

    for j in range(7):
        if dp[j]:
            temp[(i + j) % 7] = 1
            temp[j] = 1
    dp = temp

if dp[4]:
    print("YES")
else:
    print("NO")
