import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip().split())) for i in range(n)]
que = deque()
v = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            v[i][j] = 0

        if arr[i][j] == 2:
            que.append((i, j))
            v[i][j] = 0

            while que:
                x, y = que.popleft()

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx = dx + x
                    ny = dy + y

                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and v[nx][ny] == -1:
                        v[nx][ny] = v[x][y] + 1
                        que.append((nx, ny))

for i in v:
    print(*i)

