import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]
ddx = [0, 0, 1, -1]
ddy = [1, -1, 0, 0]

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(W)]
print(arr)

v = [[[0]*31 for _ in range(W)] for _ in range(H)]
que = deque([[0, 0, 0, 0]])

res = -1

while que:
    x, y, temp, h = que.pop()

    if x == H - 1 and y == W - 1:
        if res == -1:
            result = v[x][y][h]
        else:
            result = min(res, v[x][y][h])
        break

    if h < K:
        for i in range(len(dx_m)):
            new_x = x + dx_m[i]
            new_y = y + dy_m[i]

            if 0 <= new_x < H and 0 <= new_y < W and m[new_x][new_y] == 0 and visited[new_x][new_y][h + 1] == 0:
                visited[new_x][new_y][h + 1] = visited[x][y][h] + 1
                queue.append([new_x, new_y, ans + 1, h + 1])

    for i in range(len(dx_a)):
        new_x = x + dx_a[i]
        new_y = y + dy_a[i]

        if 0 <= new_x < H and 0 <= new_y < W and m[new_x][new_y] == 0 and visited[new_x][new_y][h] == 0:
            visited[new_x][new_y][h] = visited[x][y][h] + 1
            queue.append([new_x, new_y, ans + 1, h])

print(result)