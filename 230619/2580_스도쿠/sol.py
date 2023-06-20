import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

# arr = [list(map(int, input().split())) for _ in range(9)]
# # for i in arr:
# #     print(i)
#
# temp = []
# for i in range(9):
#     for j in range(9):
#         if arr[i][j] == 0:
#             temp.append((i,j))
#
#
# for i in temp:
#     row = arr[i[0]]
#     col = [row[i[1]] for row in arr]
#
#     box = []
#     x, y = i[0]//3, i[1]//3
#     for j in range(x * 3, (x+1) * 3):
#         for k in range(y * 3, (y + 1) * 3):
#             box.append(arr[j][k])
#
# def check(n):
#     if n == len(temp):
#         for i in arr:
#             print(*i)
#         exit(0)
#
#
#
#
#
#     # print(row)
#     # print(col)
#     # print(box)
#     arr1 = set(range(1, 10))
#     row1 = arr1 - set(row)
#     col1 = arr1 - set(col)
#     box1 = arr1 - set(box)
#     res = [row1,  col1, box1]
#     # while res:
#     for l in range(len(res)):
#         if len(res[l]) == 1:
#             arr[i[0]][i[1]] = list(res[l])[0]
#             res.pop(l)
#             break
# for i in arr:
#     print(*i)
#
# # print(arr)
# #             row_remain = n_list- set(row)
# #             col_remain = n_list - set(col)
# #             room_remain = n_list -set(room)






def row(x, n):
    for i in range(9):
        if n == arr[x][i]:
            return False
    return True


def col(y, n):
    for i in range(9):
        if n == arr[i][y]:
            return False
    return True


def box(x, y, n):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == arr[nx+i][ny+j]:
                return False
    return True



def check(n):

    if n == len(temp):
        for i in arr:
            print(*i)
        exit()


    for i in range(1, 10):
        x = temp[n][0]
        y = temp[n][1]

        if row(x, i) and col(y, i) and box(x, y, i):
            arr[x][y] = i
            check(n + 1)
            arr[x][y] = 0


arr = [list(map(int, input().split())) for _ in range(9)]

temp = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            temp.append((i,j))

check(0)