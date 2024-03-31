import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    v = [[0] * (n) for _ in range(n)]

    que = deque([(sx, sy)])
    v[sx][sy] = 1

    while que:
        x, y = que.popleft()
        if (x, y) == (ex, ey):
            break

        for dx, dy in ((-1, 2),(-1, -2),(-2, -1),(-2, 1),(1, 2),(1, -2),(2, -1),(2, 1)):
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                v[nx][ny] = v[x][y] + 1
                que.append((nx, ny))
    print(v[ex][ey] - 1)