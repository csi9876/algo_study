import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]


# 길이체크
def check():
    max_cnt = 0

    for i in range(n):
        # 가로 확인
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)

        # 세로 확인
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)

    return max_cnt


res = 0
for i in range(n):
    for j in range(n-1):
        # 오른쪽 교체
        if j+1 < n and arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            res = max(res, check())
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        # 아래쪽 교체
        if i + 1 < n and arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            res = max(res, check())
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(res)