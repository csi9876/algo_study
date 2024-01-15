import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

import copy


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

#    우  좌  하  상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# cctv
direction = [[],
             [[0], [1], [2], [3]],  # 1번 한방향
             [[0, 1], [2, 3]],  # 2번 양방향
             [[0, 2], [2, 1], [1, 3], [3, 0]],  # 3번 직각 방향
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]],  # 4번 세방향
             [[0, 1, 2, 3]]]    # 5번 모든 방향

# 감시 영역
def watch(y, x, dir, temp):
    # 설정 방향
    for d in dir:
        nx = x
        ny = y
        # 벽에 닿을 때까지
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < m and 0 <= ny < n and temp[ny][nx] != 6:
                if temp[ny][nx] == 0:
                    temp[ny][nx] = '#'
            else:
                break

# cctv 감시영역
def dfs(office, cnt):
    global ans

    # 사무실 복사
    temp = copy.deepcopy(office)

    # 모든 cctv 배치하면 감시 영역 카운트 및 최소값 갱신
    if cnt == cctv_cnt:
        c = 0
        for i in temp:
            c += i.count(0)
        ans = min(ans, c)
        return

    # 현재 cctv 가져오기
    y, x, cctv = que[cnt]
    # 모든 방향에 대해
    for k in direction[cctv]:
        watch(y, x, k, temp)    # 감시영역 설정
        dfs(temp, cnt + 1)      # 다음 번 cctv
        temp = copy.deepcopy(office)    # 사무실 리셋

cctv_cnt = 0
que = []
ans = int(1e9)

for i in range(n):
    for j in range(len(arr[i])):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv_cnt += 1
            que.append([i, j, arr[i][j]])

dfs(arr, 0)

print(ans)