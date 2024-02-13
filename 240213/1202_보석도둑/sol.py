import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

import heapq

n, k = map(int, input().split())
arr = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(arr, (m, v))
bag = []
for _ in range(k):
    c = int(input())
    bag.append(c)
bag.sort()
print(arr, bag)
ans = 0
res = []
for i in bag:
    while arr and i >= arr[0][0]:
        heapq.heappush(res, -heapq.heappop(arr)[1])
    if res:
        ans -= heapq.heappop(res)
    elif not arr:
        break
print(ans)