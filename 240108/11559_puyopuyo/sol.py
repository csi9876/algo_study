import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque


def check(x, y):
    que = deque([(x, y)])
    now = arr[x][y]
    pos = []

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6 and arr[nx][ny] == now and not v[nx][ny]:
                pos.append((nx, ny))
                que.append((nx, ny))
                v[nx][ny] = 1

    if len(pos) >= 4:
        pos.sort(key=lambda x: (x[1], x[0]))
        for i, j in pos:
            arr[i][j] = '_'
            bomb.append((i, j))

n = 12
arr = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0

while True:
    v = [[0] * (n//2) for _ in range(n)]
    bomb = []

    # 색이 같은 뿌요 펑
    for i in range(n):
        for j in range((n//2)):
            if arr[i][j] != '.' and arr[i][j] != '_' and not v[i][j]:
                check(i, j)

    if not len(bomb):
        break

    # 뿌요 하강
    for b in bomb:
        x, y = b[0], b[1]
        for i in range(x, 0, -1):
            arr[i][y] = arr[i - 1][y]
        arr[0][y] = '.'

    time += 1

print(time)