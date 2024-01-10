import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


import heapq


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

v = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
virus = []
heap = []

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            heapq.heappush(heap, (arr[i][j], i, j))
            v[i][j] = 1

for _ in range(s):
    next_virus = []

    while heap:
        now = heapq.heappop(heap)   # 값이 작은 바이러스부터 추출
        ck, cx, cy = now[0], now[1], now[2]

        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = ck
                    next_virus.append((ck, nx, ny))
    for vir in next_virus:
        heapq.heappush(heap, vir)     # 한번에 모두 삽입

print(arr[x-1][y-1])
