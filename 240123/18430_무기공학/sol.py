import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 방향을 나타내는 딕셔너리
dir = {0: [0, -1, 1, 0],
       1: [-1, 0, 0, -1],
       2: [-1, 0, 0, 1],
       3: [0, 1, 1, 0]}
v = [[0] * m for _ in range(n)]

res = 0


def dfs(i, j, sum):
    global res
    if j == m:      # j가 m과 같다면 다음 행으로 넘어감
        i += 1
        j = 0
    if i == n:      # i가 n과 같다면, 최대 합을 갱신하고 합 종료
        res = max(res, sum)
        return
    # 현재 위치 방문하지 않았다면
    if not v[i][j]:
        for k in range(4):
            a, b, c, d = dir[k]
            x, y, xx, yy = i+a, j+b, i+c, j+d
            if 0 <= x < n and 0 <= xx < n and 0 <= y < m and 0 <= yy < m and not v[x][y] and not v[xx][yy]:
                v[x][y] = v[xx][yy] = v[i][j] = True    # 방문
                # 다음 위치로 이동해 합 계산
                dfs(i, j+1, sum + arr[i][j] * 2 + arr[x][y] + arr[xx][yy])
                v[i][j] = v[x][y] = v[xx][yy] = False   # 방문 취소
    # 다음 위치 이동
    dfs(i, j+1, sum)


dfs(0, 0, 0)
print(res)