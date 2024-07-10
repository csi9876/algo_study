import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

import heapq

n, m = map(int, input().split())
s, e = map(int, input().split())

inf = sys.maxsize

edge = [[] for _ in range(n+1)]
ans = 0
distance = [0] * (n+1)

for _ in range(m):
    h1, h2, k = map(int, sys.stdin.readline().split())
    edge[h1].append([h2, k])
    edge[h2].append([h1, k])


h = []
heapq.heappush(h, (-inf, s))
distance[s] = inf

while h:
    dist, now = heapq.heappop(h)
    dist = - dist
    if distance[now] > dist:
        continue
    for node, d in edge[now]:
        cost = min(dist, d)
        if cost > distance[node]:
            distance[node] = cost
            heapq.heappush(h, (-cost, node))

print(distance[e])