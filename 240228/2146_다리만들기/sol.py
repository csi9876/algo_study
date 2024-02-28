import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

idx = 1

# 섬 갯수 구하고 섬마다 번호 표시
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not v[i][j]:
            que = deque()
            que.append((i, j))
            v[i][j] = 1
            arr[i][j] = idx

            while que:
                x, y = que.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < n and not v[nx][ny]:
                        if arr[nx][ny] == 1:
                            que.append((nx, ny))
                            arr[nx][ny] = idx
                            v[nx][ny] = 1
            idx += 1

# 섬 사이 최단 거리 구하기
def bfs(island):
    que = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == island:
                que.append((i, j))
                dist[i][j] = 0
    while que:
        x, y = que.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                # 다른 섬과 만난 경우
                if arr[nx][ny] != island and arr[nx][ny] != 0:
                    return dist[x][y]
                # 물이고 아직 건너지 않은 곳일 경우
                if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    que.append((nx, ny))


res = sys.maxsize
for island in range(1, idx):
    res = min(res, bfs(island))

print(res)
