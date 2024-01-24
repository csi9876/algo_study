import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

v = [[0] * n for _ in range(n)]

que = deque([])
que.append((0, 0))
v[0][0] = 1

while que:
    x, y = que.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
            if arr[nx][ny] == 1:    # 길이면
                v[nx][ny] = v[x][y]     # 현재 값 유지
                que.appendleft((nx, ny))    # 맨 앞에 삽입
            else:   # 벽이면
                v[nx][ny] = v[x][y] + 1     # 현재 값 + 1
                que.append((nx, ny))    # 맨 뒤에 삽입

print(v[n - 1][n - 1] - 1)  # 시작이 1이므로 -1