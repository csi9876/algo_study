import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    maxn = arr[-1]

    for i in range(n-2, -1, -1):
        if arr[i] > maxn:
            maxn = arr[i]
        else: res += maxn - arr[i]
    print(res)