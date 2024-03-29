import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
arr = [list((input().strip())) for _ in range(n)]
res = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):

  que = deque()
  que.append((a, b))
  v = [[-1] * m for _ in range(n)]
  v[a][b] = 0
  temp = 0
  while que:
    x, y = que.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == -1 and arr[nx][ny] == 'L':
        v[nx][ny] = v[x][y] + 1
        temp = max(temp, v[nx][ny])
        que.append((nx, ny))
  return temp


for i in range(n):
  for j in range(m):
    if arr[i][j] == 'L':
      res = max(res, bfs(i, j))
print(res)