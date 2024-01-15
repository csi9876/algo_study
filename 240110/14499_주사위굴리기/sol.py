import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

'''
       513462
326154 123456 421653
       263415
'''
#
#
#


n, m, x, y, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dir = list(map(int, input().split()))
v = [0] * 6

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for k in dir:
    nx = x + dx[k - 1]
    ny = y + dy[k - 1]

    if 0 <= nx < n and 0 <= ny < m:
        # 이동 방향에 맞게 주사위 변경
        if k == 1:  # 동
            v = [v[3], v[1], v[0], v[5], v[4], v[2]]
        elif k == 2:   # 서
            v = [v[2], v[1], v[5], v[0], v[4], v[3]]
        elif k == 3:  # 북
            v = [v[4], v[0], v[2], v[3], v[5], v[1]]
        elif k == 4:    # 남
            v = [v[1], v[5], v[2], v[3], v[0], v[4]]

        # 지도 값이 0이면 주사위값 복사
        if arr[nx][ny] == 0:
            arr[nx][ny] = v[-1]
        else:   # 주사위 바닥에 지도 값 복사 후 0으로 변경
            v[-1] = arr[nx][ny]
            arr[nx][ny] = 0

        print(v[0])
        x, y = nx, ny

