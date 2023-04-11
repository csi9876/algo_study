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

# def findset(x):     # x가 속한 집합의 대표 리턴
#     while x != rep[x]:
#         x = rep[x]
#         return x
#
# def union(x, y):        # y의 대표원소가 x의 대표원소를 가리키도록 함
#     rep[findset(y)]=findset(x)


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
pare = [-1]*(N+1)
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
                pare[dd] = start
                # print(path)
                heappush(que, (res, dd))


# print(path)
ik(0,S)

result = []
idx = E
while idx != S:
    result.append(idx)
    idx = pare[idx]

result.append(S)
result.reverse()

print(v[E])
print(len(result))
print(*result)
