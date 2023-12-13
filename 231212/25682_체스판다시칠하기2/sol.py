import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(input()))

res = int(1e9)

for c in ["W", "B"]:        # w시작, b시작
    v = [[0] * (m+1) for _ in range(n+1)]       # 누적합 저장을 위한 배열
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0:      # 보드의 열과 행을 더해서 짝수면 시작 색과 다르다
                temp = arr[i][j] != c
            else:
                temp = arr[i][j] == c   # 홀수면 시작 c와 같다
            v[i+1][j+1] = v[i][j+1] + v[i+1][j] - v[i][j] + temp    # 2차원 배열의 누적합

    cnt = int(1e9)
    for i in range(1, n-k + 2):
        for j in range(1, m-k + 2):
            cnt = min(cnt, v[i+k-1][j+k-1] - v[i+k-1][j-1] - v[i-1][j+k-1] + v[i-1][j-1])
            # 2차원 배열의 누적합에 k 적용
    res = min(cnt, res)

print(res)