import sys
sys.stdin = open('input.txt')

# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(M)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# v = [[0 for _ in range(M)] for _ in range(N)]
#
#
# ### ㅡ, ㄴ, ㅁ, ㅐ
# def tet4(x, y, n, cnt):
#     global t4
#     if cnt == 4:
#         if t4 < n:
#             t4 = n
#     else:
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#
#             if 0 <= nx < N and 0 <= ny < M:
#                 if v[nx][ny] == 0:
#                     v[nx][ny] = 1
#                     tet4(nx, ny, n + arr[nx][ny], cnt + 1)
#                     v[nx][ny] = 0
#
# # ㅜ
# def tet1(x,y):
#     global t1
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < N and 0 <= ny < M:
#             nx2 = nx + dx[k]
#             ny2 = ny + dy[k]
#             if 0 <= nx2 < N and 0 <= ny2 < M:
#                     for h in [-1, 1]:
#                         temp = arr[x][y]
#                         if k == 0 or k == 1: # ㅓ
#                             nyh = ny + h
#                             if 0 <= nyh < M:
#                                 temp += arr[nx][ny]
#                                 temp += arr[nx2][ny2]
#                                 temp += arr[nx][nyh]
#                         elif k == 2 or k == 3: # ㅗ
#                             nxh = nx + h
#                             if 0 <= nxh < N:
#                                 temp += arr[nx][ny]
#                                 temp += arr[nx2][ny2]
#                                 temp += arr[nxh][ny]
#                         if t1 < temp:
#                             t1 = temp
#
#
# res = 0
# for i in range(N):
#     for j in range(M):
#         t4 = 0
#         t1 = 0
#         v[i][j] = 1
#         tet4(i, j, arr[i][j], 1)
#         v[i][j] = 0
#         tet1(i, j)
#         t5 = max(t4, t1)
#         res = max(t5, res)
#
# print(res)




import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = []
for i in range(N):
    arr.append([int(x) for x in input().split()])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

v = [[0 for _ in range(M)] for _ in range(N)]

# ㅡ, ㄴ, ㅐ, ㅁ
def tet4(x,y,n,c):
    global t4
    if c == 4:
        if t4 < n:
            t4 = n
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if v[nx][ny] == 0:
                    v[nx][ny] = 1
                    tet4(nx,ny,n + arr[nx][ny],c + 1)
                    v[nx][ny] = 0

# ㅜ
def tet1(x,y):
    global t1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            nnx = nx + dx[k]
            nny = ny + dy[k]
            if 0 <= nnx < N and 0 <= nny < M:
                    for h in [-1, 1]:
                        value = arr[x][y]
                        if k == 0 or k == 1:  # ㅓ
                            sny = ny + h
                            if 0 <= sny < M:
                                value += arr[nx][ny]
                                value += arr[nnx][nny]
                                value += arr[nx][sny]
                        elif k == 2 or k == 3:   # ㅗ
                            snx = nx + h
                            if 0 <= snx < N:
                                value += arr[nx][ny]
                                value += arr[nnx][nny]
                                value += arr[snx][ny]
                        if t1 < value:
                            t1 = value

res = 0
for i in range(N):
    for j in range(M):
        t4 = 0
        t1 = 0
        v[i][j] = 1
        tet4(i,j,arr[i][j],1)
        v[i][j] = 0
        tet1(i, j)
        t5 = max(t1, t4)
        res = max(res, t5)

print(res)