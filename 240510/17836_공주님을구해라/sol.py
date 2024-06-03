import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n, m, t = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [list(map(int, input().split())) for _ in range(n)]
que = deque()
visited = [[0] * m for _ in range(n)]


def bfs():
    gram = 10001
    que.append((0, 0))
    visited[0][0] = 1

    while que:
        x, y = que.popleft()

        # 공주 도착
        if (x, y) == (n - 1, m - 1):
            return min(visited[x][y] - 1, gram)

        # 그람이 있는 곳에 도착했을 때
        # 공주까지 쭉 가기
        if arr[x][y] == 2:
            gram = visited[x][y] - 1 + n - 1 - x + m - 1 - y

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == 0 or arr[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))

    return gram


res = bfs()

if res > t:
    print('Fail')
else:
    print(res)