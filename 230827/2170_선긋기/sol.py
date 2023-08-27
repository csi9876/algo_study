import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


N = int(input())
arr = []
for n in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort()
# print(arr)

start, end = arr[0]
res = 0
for s, e in arr:
    if end < s:
        res += end-start
        start, end = s, e
        continue
    end = max(end, e)
res += end-start
print(res)