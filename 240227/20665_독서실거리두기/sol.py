import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, t, p = map(int, input().split())
arr = []
for _ in range(t):
    s, e = map(int, input().split())
    arr.append((s, e))
arr.sort()
print(arr)
