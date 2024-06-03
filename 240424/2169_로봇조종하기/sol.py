import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for i in range(N)]

# 맨 윗줄
for j in range(1, M):
    arr[0][j] += arr[0][j - 1]

# 나머지
for i in range(1, N):
    l = [arr[i][j] + arr[i - 1][j] for j in range(M)]
    r = [arr[i][j] + arr[i - 1][j] for j in range(M)]

    # 우
    for j in range(1, M):
        l[j] = max(l[j], l[j - 1] + arr[i][j])

    # 좌
    for j in range(M - 2, -1, -1):
        r[j] = max(r[j], r[j + 1] + +arr[i][j])

    # 선택
    for j in range(M):
        arr[i][j] = max(l[j], r[j])

print(arr[-1][-1])