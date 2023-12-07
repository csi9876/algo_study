import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

import heapq

n ,h, t = map(int, input().split())
arr = []
for _ in range(n):
    h2 = int(input())
    heapq.heappush(arr, -h2)

cnt = 0

for _ in range(t):
    max_h = heapq.heappop(arr)*-1
    if max_h == 1:
        heapq.heappush(arr, -1)
    elif max_h < h:
        heapq.heappush(arr, max_h*-1)
        break
    else:
        heapq.heappush(arr, (max_h//2)*-1)
        cnt += 1

res = heapq.heappop(arr)*(-1)
if res >= h:
    print("NO")
    print(res)
else:
    print("YES")
    print(cnt)