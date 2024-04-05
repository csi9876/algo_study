import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from heapq import heappop, heappush

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        arr[b].append([a, s])

    INF = float('inf')
    que = []
    dist = [INF for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]
    dist[c] = 0
    heappush(que, [0, c])

    while que:
        cost, node = heappop(que)
        if visited[node] == 1:
            continue
        visited[node] = 1
        for next, d in arr[node]:
            if not visited[next]:
                if dist[next] > cost + d:
                    dist[next] = cost + d
                    heappush(que, [dist[next], next])

    cnt = 0
    time = 0
    for c in range(1, n + 1):  # 방문 완료 도시의 개수 세기, 방문한 도시들 중 가장 시간이 큰 것(최단거리 중에서 최wkd거리)
        if visited[c]:
            cnt += 1
            time = max(time, dist[c])

    print(cnt, time)