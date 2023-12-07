import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]


dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,1,-1,-1,0,1]
idx = []

def bfs(x, y, checkidx):
    q=deque([(x,y)])
    v[x][y]=1
    check=[(x, y)]
    while q:
        x, y= q.popleft()
        for i in range(8):
            nx, ny= x+dx[i], y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if v[nx][ny]==1:
                continue
            if arr[x][y]<arr[nx][ny]:
                return 0
            if arr[x][y]==arr[nx][ny]:
                v[nx][ny]=1
                q.append((nx,ny))
                check.append((nx,ny))
        checkidx+=check
    return 1

res = 0
for i in range(N):
    for j in range(M):
        if (i, j) not in idx:
            v = [[0]*M for _ in range(N)]
            res += bfs(i, j, idx)
print(res)
