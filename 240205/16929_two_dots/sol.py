import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(str(input().rstrip())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

v = [[False for _ in range(m)] for _ in range(n)]
ans = 0

def solve(temp, x, y, cnt):
    global ans
    if ans:
        print("Yes")
        exit()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 이동횟수 4회 이상 + 원위치 복귀 하면 사이클 완성
        elif cnt >= 4 and nx == sx and ny == sy:
            ans = 1
            print("Yes")
            exit()
        # 미방문이면 방문 표시하고 다음 위치 이동
        if arr[nx][ny] == temp and v[nx][ny] == False:
            v[nx][ny] = True
            solve(temp, nx, ny, cnt+1)
            v[nx][ny] = False

for i in range(n):
    for j in range(m):
        v[i][j] = True
        sx, sy = i, j
        solve(arr[i][j], i, j, 1)
        v[i][j] = False

print("No")