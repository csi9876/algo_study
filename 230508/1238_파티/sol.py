import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from heapq import heappop, heappush


# 자기 마을에서 X번 마을로 오고 가는 최단 경로
# 다이스트라 n번 반복 시작점을 자기 위치 끝 점 dd가 X면 종료

N, M, X = map(int, input().split())
arr = [[]for _ in range(N+1)]
# print(arr)

for _ in range(M):
    s, e, t = map(int, input().split())
    arr[s].append((t, e))

# print(arr)
v = [int(1e9)]*(N+1)
# print(v)

# 각 마을에서 목적지 최단 경로
def ik(cost, start):
    que = []
    heappush(que, (cost, start))

    while que:
        cost, now = heappop(que)

        for cc, dd in arr[now]:
            res = cost + cc
            if res > v[dd]:
                continue
            v[dd] = res
            # if dd == X:
            #     return res
            heappush(que, (res, dd))

# 목적지에서 다시 출발지로 돌아오는 최단경로
def ik1(cost, start):
    que = []
    heappush(que, (cost, start))

    while que:
        cost, now = heappop(que)

        for cc, dd in arr[now]:
            res = cost + cc
            if res > v[dd]:
                continue
            v[dd] = res
            heappush(que, (res, dd))


result = [0for _ in range(N+1)]
# print(result)
for i in range(1, N+1):
    v = [int(1e9)] * (N + 1)
    v[i] = 0
    ik(0,i)
    result[i]=v[X]

# print(result)

v = [int(1e9)] * (N + 1)
v[X] = 0
ik1(0,X)
# print(v)

for i in range(N):
    result[i+1] += v[i+1]

print(max(result))