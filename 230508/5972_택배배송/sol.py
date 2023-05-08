import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int,input().split())
# print(N, M)
arr = [[]for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    arr[s].append((w, e))
    arr[e].append((w, s))
# print(arr)
v = [int(1e9)]*(N+1)

for cost, start in arr[1]:
    que = []
    heappush(que, (cost, start))
    if start == N:
        v[N] = cost
        break
    while que:
        cost, now = heappop(que)
        for cc, dd in arr[now]:
            res = cost+cc
            if res >= v[dd]:
                continue
            v[dd] = res
            heappush(que, (res, dd))
print(v[N])

# cost, start =
# heappush()que, ()

# def ik(cost, start):
#     que = []
#     heappush(que, (cost, start))
#
#     while que:
#         cost, now = heappop(que)
#
#         for cc, dd in arr[now]:
#             res = cost + cc
#             if res > v[dd]:
#                 continue
#             v[dd] = res
#             # if dd == X:
#             #     return res
#             heappush(que, (res, dd))
#
# # 목적지에서 다시 출발지로 돌아오는 최단경로
# def ik1(cost, start):
#     que = []
#     heappush(que, (cost, start))
#
#     while que:
#         cost, now = heappop(que)
#
#         for cc, dd in arr[now]:
#             res = cost + cc
#             if res > v[dd]:
#                 continue
#             v[dd] = res
#             heappush(que, (res, dd))
#
#
# result = [0for _ in range(N+1)]
# # print(result)
# for i in range(1, N+1):
#     v = [int(1e9)] * (N + 1)
#     v[i] = 0
#     ik(0,i)
#     result[i]=v[X]
#
# # print(result)
#
# v = [int(1e9)] * (N + 1)
# v[X] = 0
# ik1(0,X)
# # print(v)
#
# for i in range(N):
#     result[i+1] += v[i+1]
#
# print(max(result))