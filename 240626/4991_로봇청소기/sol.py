import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

import copy

r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]
mist = []  # 공기청정기 위치 저장할 리스트
count = 0  # 공기청정기 개수 세기

# 공기청정기 위치 찾기
for i in range(r):
    if arr[i][0] == -1:
        count += 1
        mist.append(i)
    if count == 2:
        break

# 우 상 좌 하 방향 정의
cx = [0, -1, 0, 1]
cy = [1, 0, -1, 0]

# 우 하 좌 상 방향 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check():
    global arr

    v = [[0] * c for _ in range(r)]  # 새로운 배열 생성
    for i in range(r):
        for j in range(c):
            x, y = i, j
            count = 0
            if arr[x][y] == 0:  # 공기청정기가 아닌 경우
                continue
            if arr[x][y] == -1:  # 공기청정기인 경우
                v[x][y] = -1
                continue

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                    count += 1
                    v[nx][ny] += int(arr[x][y] // 5)  # 미세먼지 확산
            v[x][y] += (arr[x][y] - int(arr[x][y] // 5) * count)  # 미세먼지 확산 후 남은 양

    arr = copy.deepcopy(v)  # 새로운 배열로 업데이트

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
        arr[x][y], temp = temp, arr[x][y]  # 공기청정기 작동
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

        arr[x][y], temp1 = temp1, arr[x][y]  # 공기청정기 작동
        x, y = nx, ny


for i in range(t):
    check()  # 미세먼지 확산
    search()  # 공기청정기 작동

res = 0

for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            res += arr[i][j]  # 남은 미세먼지 합 계산

print(res)