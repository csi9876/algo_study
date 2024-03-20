import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 0
time = 0

for x, y in arr:
    if time <= x:
        cnt += 1
        time = y
    else:
        continue

print(cnt)