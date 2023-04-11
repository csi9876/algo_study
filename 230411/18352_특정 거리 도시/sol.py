import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from heapq import heappop, heappush



N, M, K, X = map(int, input().split())
arr = [[]for _ in range(N+1)]
# print(arr)
for i in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)

# print(arr)
v = [int(1e9)] * (N+1)
v[X] = 0

def ik(cost, start):
    que = []
    heappush(que, (cost, start))

    while que:
        cost, now = heappop(que)
        if v[now] < cost:
            continue
        for i in arr[now]:
            res = cost + 1
            if res < v[i]:
                v[i] = res
                heappush(que,(res, i))


ik(0, X)
# print(v)

count = 0
for i in range(len(v)):
    if v[i] == K:
        print(i)
        count += 1
if count == 0:
    print(-1)