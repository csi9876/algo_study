import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())


# 방문 표시
v = [[[0] * 5 for _ in range(n)] for _ in range(m)]
v[sx-1][sy-1][sd] = 1
que = deque()
que.append((sx-1, sy-1, sd, 0))

while que:
    x, y, d, cnt = que.popleft()
    # 도착하면 출력
    if (x, y, d) == (ex - 1, ey - 1, ed):
        print(cnt)
        break

    # 1~3 칸 이동
    for dis in range(1, 4):
        nx = x + dx[d] * dis
        ny = y + dy[d] * dis
        nd = d
        # 범위 벗어나고, 벽이면 정지
        if not (0 <= nx < m and 0 <= ny < n) or arr[nx][ny]:
            break
        # 이미 방문했으면 건너뛰기
        if v[nx][ny][nd]:
            continue
        que.append((nx, ny, nd, cnt + 1))
        v[nx][ny][nd] = 1

    # 동, 서 방향일 때는 남, 북 회전 가능
    if d == 1 or d == 2:
        if not v[x][y][3]:
            v[x][y][3] = 1
            que.append((x, y, 3, cnt + 1))
        if not v[x][y][4]:
            v[x][y][4] = 1
            que.append((x, y, 4, cnt + 1))
    else:   # 남, 북 방향일 때는 동, 서 회전 가능
        if not v[x][y][1]:
            v[x][y][1] = 1
            que.append((x, y, 1, cnt + 1))
        if not v[x][y][2]:
            v[x][y][2] = 1
            que.append((x, y, 2, cnt + 1))