import sys, copy
sys.stdin = open('input.txt')
from collections import deque

#
# R, C, T = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(R)]
# mist = []
# # count = 0
#
# for i in range(R):
#     if arr[i][0] == -1:
#         # count += 1
#         mist.append(i)
#     # if count == 2:
#     #     break
#
#     # 우상좌하
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]
#
#
#     # 우하좌상
# cx = [0, 1, 0, -1]
# cy = [1, 0, -1, 0]
#
# def check():
#     bit = [[0]*C for _ in range(R)]
#     for i in range(R):
#         for j in range(C):
#             count = 0
#             if arr[i][j] == 0:
#                 continue
#             if arr[i][j] == -1:
#                 bit[i][j] = -1
#                 continue
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
#                     count += 1
#                     bit[nx][ny] += int(arr[i][j] // 5)
#             bit[i][j] += (arr[i][j] - int(arr[i][j] // 5) * count)
#
#     for i in range(R):
#         for j in range(C):
#             arr[i][j] = bit[i][j]
#
# def search():
#     now, dir = 0, 0
#     x, y = mist[0], 1
#     while True:
#         nx = x + dx[dir]
#         ny = y + dy[dir]
#         if x == mist[0] and y == 0:
#             break
#         if nx < 0 or nx >= R or ny < 0 or ny >= C:
#             dir += 1
#             continue
#         arr[x][y], now = now, arr[x][y]
#         x, y = nx, ny
#
#     now1, dir1 = 0, 0
#     x, y = mist[1], 1
#
#     while True:
#         nx = x + cx[dir]
#         ny = y + cy[dir]
#         if x == mist[1] and y == 0:
#             break
#         if nx < 0 or nx >= R or ny < 0 or ny >= C:
#             dir1 += 1
#             continue
#         arr[x][y], now = now, arr[x][y]
#         x, y = nx, ny
#
#
# for i in range(T):
#     check()
#     search()
#
#
# result = 0
#
# for i in range(R):
#     for j in range(C):
#         if arr[i][j] > 0:
#             result += arr[i][j]
#
# print(result)


import sys, copy
input = sys.stdin.readline

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]
mist = []
count = 0

for i in range(r):
    if arr[i][0] == -1:
        count += 1
        mist.append(i)
    if count == 2:
        break
# 우 상 좌 하
cx = [0, -1, 0, 1]
cy = [1, 0, -1, 0]

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check():
    global arr
    bit = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            x, y = i, j
            count = 0
            if arr[x][y] == 0:
                continue
            if arr[x][y] == -1:
                bit[x][y] = -1
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                    count += 1
                    bit[nx][ny] += int(arr[x][y] // 5)
            bit[x][y] += (arr[x][y] - int(arr[x][y] // 5) * count)

    arr = copy.deepcopy((bit))

def search():
    temp, dir = 0, 0
    x, y = mist[0], 1
    while True:
        nx = x + cx[dir]
        ny = y + cy[dir]
        if x == mist[0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue
        arr[x][y], temp = temp, arr[x][y]
        x, y = nx, ny

    temp1, dir1 = 0, 0
    x, y = mist[1], 1
    while True:
        nx = x + dx[dir1]
        ny = y + dy[dir1]
        if x == mist[1] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir1 += 1
            continue

        arr[x][y], temp1 = temp1, arr[x][y]
        x, y = nx, ny


for i in range(t):
    check()
    search()

result = 0

for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            result += arr[i][j]

print(result)