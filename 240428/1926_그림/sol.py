import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip().split())) for i in range(n)]

que = deque()
v = [[0 for _ in range(m)] for _ in range(n)]
res = 0
max_n = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and v[i][j] == 0:
            que.append((i, j))
            res += 1

            v[i][j] = 1

            temp = 1

            while que:
                x, y = que.popleft()

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx = dx + x
                    ny = dy + y
                    if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == 0 and arr[nx][ny] == 1:
                        que.append((nx, ny))
                        v[nx][ny] = 1
                        temp += 1

            max_n = max(max_n, temp)

print(res)
print(max_n)
