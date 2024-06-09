import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

while True:
    if arr[r][c] == 0:
        cnt += 1
        arr[r][c] = 2

    # 4방향 탐색
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽으로 90도 회전
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            r, c = nx, ny
            break
    else:
        # 4방향 모두 청소되어 있거나 벽인 경우
        nx = r - dx[d]
        ny = c - dy[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1:
            r, c = nx, ny
        else:
            break

print(cnt)
