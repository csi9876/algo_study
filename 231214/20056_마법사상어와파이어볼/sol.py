import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
for _ in range(m):
    a, b, c, d, e = map(int, input().split())
    arr.append((a, b, c, d, e))
print(arr)