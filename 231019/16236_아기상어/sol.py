import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            x, y = i, j
        elif arr[i][j]:
            count += 1

size = 2
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, v):
    v[x][y] = 1
    que = deque()
    que.append((x, y, 0))
    temp = 0
    selected = (N, N, -1)
    while que:
        x, y, s = que.popleft()
        if temp != s and selected[-1] != -1:
            return selected
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or v[nx][ny] or arr[nx][ny] > size:
                continue
            if arr[nx][ny] and arr[nx][ny] < size:
                selected = min(selected, (nx, ny, s+1))
            v[nx][ny] = 1
            que.append((nx, ny, s+1))
        temp = s
    return (-1, -1, -1)


result, count = 0, 0
arr[x][y] = 0
while 1:
    que = [[0] * N for _ in range(N)]
    x, y, s = bfs(x, y, que)
    if s == -1:
        break
    arr[x][y] = 0
    result += s
    count += 1
    if count == size:
        size += 1
        count = 0

print(result)