import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

que = deque()
v = []

# 적구슬, 청구슬 위치 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        if arr[i][j] == 'B':
            bx, by = i, j
cnt = 1
que.append([rx, ry, bx, by, cnt])
v.append([rx, ry, bx, by])

# 구슬 이동
def move(x, y, i, j):
    count = 0
    # 다음 위치가 벽이 아니고 현재 위치가 구멍이 아닌 곳까지 이동
    while arr[x+i][y+j] != '#' and arr[x][y] != 'O':
        x += i
        y += j
        count += 1
    return x, y, count

# bfs
def solve():
    while que:
        rx, ry, bx, by, cnt = que.popleft()

        if cnt > 10:    # 10번 초과로 움직이면 종료
            break

        for i in range(4):
            nrx, nry, rCnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bCnt = move(bx, by, dx[i], dy[i])

            # 파란돌 구멍에 빠지면 실패
            if arr[nbx][nby] == 'O':
                continue
            # 빨간돌 구멍에 빠지면 성공
            if arr[nrx][nry] == 'O':
                return cnt

            # 빨간돌 파란돌 위치 겹치면
            if nrx == nbx and nry == nby:
                if rCnt > bCnt:  # 더 많이 이동한 구슬을 한 칸 뒤로 물리기
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            # 방문하지 않았으면 방문 표시
            if [nrx, nry, nbx, nby] not in v:
                v.append([nrx, nry, nbx, nby])
                que.append([nrx, nry, nbx, nby, cnt+1])
    return -1


print(solve())