import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, *dire = map(int, input().split())

dx = [0, 0, -1, 1]   # 동, 서, 남, 북
dy = [1, -1, 0, 0]   # 동, 서, 남, 북

# 2n+1 크기의 2차원 배열, 방문 체크
arr = [[0] * (2*n+1) for _ in range(2*n+1)]
ans = 0

def dfs(x, y, per, cnt):
    global ans
    if cnt == n:    # 모든 이동 완료하면 확률 더하기
        ans += per
        return

    np = per

    arr[x][y] = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 범위 안이고 방문하지 않았다면
        if 0 <= nx < (2*n+1) and 0 <= ny < (2*n+1) and arr[nx][ny] != 1:
            # 해당 좌표에서 확률, 이동횟수 추가하여 다시 탐색
            dfs(nx, ny, np*(dire[k]/100), cnt + 1)
            arr[nx][ny] = 0     # 방문 좌표 다시 초기화

dfs(n, n, 1, 0)

print(ans)