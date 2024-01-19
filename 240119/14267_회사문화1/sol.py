import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
res = [0] * (n + 1)

for _ in range(m):
    i, w = map(int, input().split())
    res[i] += w


for i in range(2, n + 1):
    res[i] += res[arr[i]]

print(*res[1:])