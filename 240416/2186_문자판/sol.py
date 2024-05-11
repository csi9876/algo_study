import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
s = input().strip()

dp = [[[-1 for _ in range(len(s))] for _ in range(m)] for _ in range(n)]


def dfs(idx, y, x):
    # memoization 되어있는 경우 바로 결과 반환
    if dp[y][x][idx] != -1:
        return dp[y][x][idx]

    # 글자가 완성되는 경우 카운트 추가
    if idx == len(s) - 1:
        return 1

    cnt = 0
    # 기점으로 앞으로의 경우의 수 카운트
    for step in range(1, k + 1):
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + step * dy, x + step * dx

            # 다음 문자가 일치하는 경우만 재귀 호출
            if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == s[idx + 1]:
                cnt += dfs(idx + 1, ny, nx)

    # 경우의 수 memoization 업데이트
    dp[y][x][idx] = cnt
    return cnt


res = 0

# 모든 좌표에 대해 시작 문자와 일치하는 경우 dfs 호출
for i in range(n):
    for j in range(m):
        if arr[i][j] == s[0]:
            res += dfs(0, i, j)

print(res)