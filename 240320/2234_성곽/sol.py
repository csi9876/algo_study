import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for i in range(m)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(x, y):
    que = deque()
    que.append([x, y])
    v[x][y] = 1
    room = 1
    while que:
        x, y = que.popleft()
        wall = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 비트 마스크로 벽이 없는 방향 탐색
            if (arr[x][y] & wall) != wall:
                if 0 <= nx < m and 0 <= ny < n and not v[nx][ny]:
                    room += 1
                    v[nx][ny] = 1
                    que.append([nx, ny])
            wall = wall * 2     # 다음 벽의 위치를 확인하기 위해 비트를 왼쪽으로 이동
    return room


roomCnt = 0     # 방의 총 수
maxRoom = 0     # 가장 큰 방의 크기
delRoom = 0     # 벽을 하나 제거했을 때 얻을 수 있는 가장 큰 방의 크기

# 모든 곳에 bfs해서 방의 수와 가장 큰 방 계산
for i in range(m):
    for j in range(n):
        if v[i][j] == 0:
            roomCnt += 1
            maxRoom = max(maxRoom, bfs(i, j))

# 벽을 하나씩 제거하며 bfs해서 가장 큰 방 계산
for i in range(m):
    for j in range(n):
        num = 1
        while num < 9:  # 비트마스크로 벽 존재 확인
            if num & arr[i][j]:     # 현위치에 벽이 있는 경우
                v = [[0] * n for _ in range(m)]
                arr[i][j] -= num    # 벽제거
                delRoom = max(delRoom, bfs(i, j))   # bfs
                arr[i][j] += num    # 벽 복원
            num *= 2    # 다음 방향 벽 확인 위해 비트를 왼쪽으로 이동

print(roomCnt)
print(maxRoom)
print(delRoom)