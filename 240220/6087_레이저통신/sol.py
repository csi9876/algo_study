import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

m, n = map(int, input().split())
arr = []
crr = []

for i in range(n):
    arr.append(list(input().strip()))
    for j in range(m):
        if arr[i][j] == "C":
            crr.append((i, j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

s = crr[0]
e = crr[1]

# 방문 여부와 거울 갯수 체크, 시간 단축을 위해 3차원
v = [[[int(1e9)] * 4 for _ in range(m)] for _ in range(n)]

def bfs(s):
    x, y = s
    # 시작 위치 4방향 큐
    que = deque([(x, y, k) for k in range(4)])
    for k in range(4):
        v[x][y][k] = 0

    while que:
        x, y, z = que.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # 범위 내에 있고 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '*':
               # 이전 방향과 같다면 거울의 수는 변하지 않고 다르면 추가
                if z == k:
                    cost = v[x][y][z]
                else:
                    cost = v[x][y][z] + 1
                # 새 경로가 더 적은 거울을 사용하면 방문체크하고 큐에 넣기
                if v[nx][ny][k] > cost:
                    v[nx][ny][k] = cost
                    que.append((nx, ny, k))

bfs(s)
print(min(v[e[0]][e[1]]))