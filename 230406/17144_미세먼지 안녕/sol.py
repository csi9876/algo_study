import sys, copy
sys.stdin = open('input.txt')
from collections import deque
# 미세먼지 확산, arr//5
# 남은 미세먼지 양은 arr - (arr/5)*방향 개수
# 공기청정기 작동
# 위쪽은 반시계/ 아래쪽은 시계
# 바람 방향대로 모두 한칸 씩 미세먼지 이동
# 공기청정기 = -1
#



# import sys, copy
# def check1():
#     temp1 = 0
#     dir1 = 0
#     x, y = mist[0][0], 1
#     while True:
#         nx = x + dx[dir1]
#         ny = y + dy[dir1]
#         if x == mist[0][0] and y == 0:
#             break
#         if nx < 0 or nx >= R or ny < 0 or ny >= C:
#             dir1 += 1
#             continue
#         arr[x][y], temp1 = temp1, arr[x][y]
#         x, y = nx, ny
#
# def check2():
#     temp2 = 0
#     dir2 = 0
#     x, y = mist[1][0], 1
#     while True:
#         nx = x + cx[dir2]
#         ny = y + cy[dir2]
#         if x == mist[1][0] and y == 0:
#             break
#         if nx < 0 or nx >= R or ny < 0 or ny >= C:
#             dir2 += 1
#             continue
#         arr[x][y], temp2 = temp2, arr[x][y]
#         x, y = nx, ny
# #



R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
# print(arr)
def search(arr):
    bit = [[0]*C for _ in range(R)]
    # bit = copy.deepcopy(arr)
    for i in range(R):
        for j in range(C):
            temp = 0
            if arr[i][j] == -1:
                bit[i][j] = -1
                continue
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0 <= nx < R and 0<= ny <C and arr[nx][ny] != -1:
                    temp += 1
                    bit[nx][ny] += arr[i][j]//5
            bit[i][j] += arr[i][j] - (arr[i][j]//5) * temp
    arr = copy.deepcopy(bit)

def check():
    temp1 = 0
    dir1 = 0
    que1 = deque()
    que1.append((mist[0][0],1))
    while que1:
        x, y = que1.popleft()
        if x == mist[0][0] and y == 0:
            break
        nx = x + dx[dir1]
        ny = y + dy[dir1]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir1 += 1
            continue
        arr[x][y], temp1 = temp1, arr[x][y]
        que1.append((nx,ny))


    temp2 = 0
    dir2 = 0
    que2 = deque()
    que2.append((mist[1][0], 1))
    while que2:
        x, y = que2.popleft()
        if x == mist[1][0] and y == 0:
            break
        nx = x + cx[dir2]
        ny = y + cy[dir2]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            dir2 += 1
            continue
        arr[x][y], temp2 = temp2, arr[x][y]
        que2.append((nx,ny))




mist = []
count = 0

    # 우상좌하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


    # 우하좌상
cx = [0, 1, 0, -1]
cy = [1, 0, -1, 0]
dir2 = 0



for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            mist.append((i,j))

# print(mist)


for _ in range(T):
    search(arr)
    check()




result = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            result += arr[i][j]
print(result)