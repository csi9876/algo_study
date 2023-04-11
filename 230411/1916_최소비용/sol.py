import sys
sys.stdin = open('input.txt')

# import sys
# input = sys.stdin.readline
# from heapq import heappop, heappush
#
# N = int(input())
# M = int(input())
# arr = [[]for _ in range(N+1)]
# for _ in range(M):
#     s, e, c = map(int, input().split())
#     arr[s].append((c,e))
#
# S, E = map(int,input().split())
# v = [int(1e9)] * (N+1)
# v[S] = 0
# def ik(start):
#     que = []
#     heappush(que,start)
#
#
#     while que:
#         cost, start = heappop(que)
#         if v[start] < cost:
#             continue
#         for i in arr[start]:
#             res = cost + i[0]
#             if res < v[i[1]]:
#                 v[i[1]] = res
#                 heappush(que, (res, i[1]))
#
#
# ik((0,S))
# print(v[E])




import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
M = int(input())
arr = [[]for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    arr[s].append((c, e))

S, E = map(int,input().split())
v = [int(1e9)] * (N+1)
v[S] = 0
def ik(cost, start):
    que = []
    heappush(que,(cost, start))


    while que:
        cost, start = heappop(que)
        if v[start] < cost:
            continue
        for cc, dd in arr[start]:
            res = cost + cc
            if res < v[dd]:
                v[dd] = res
                heappush(que, (res, dd))


ik(0,S)
print(v[E])