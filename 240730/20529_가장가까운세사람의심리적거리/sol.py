import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline


n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

print(arr)