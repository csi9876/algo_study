import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 1, 1, 0, -1]

v = [[0] * n for _ in range(m)]

cnt = 0
que = []

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] == 0:
            que.append((i, j))
            v[i][j] = 1
            cnt += 1

            while que:
                x, y = que.pop(0)

                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n and v[nx][ny] == 0 and arr[nx][ny] == 1:
                        v[nx][ny] = 1
                        que.append((nx, ny))

print(cnt)

