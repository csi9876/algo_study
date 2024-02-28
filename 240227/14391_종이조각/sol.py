import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n, m = map(int, input().rstrip().split())

arr = [list(map(int, input().strip())) for _ in range(n)]
ans = []

# 1 << n*m 만큼 반복, 이는 모든 경우의 수
for i in range(1 << n*m):
    total = 0

    #   가로합
    for row in range(n):
        row_sum = 0
        for col in range(m):
            # idx는 2차원 행렬을 1줄로 만들었을 때의 인덱스
            idx = row*m + col
            if i & (1 << idx) != 0:     # i & (1 << idx) != 0이면 가로로 더한다.
                row_sum = row_sum * 10 + arr[row][col]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum

    #   세로합
    for col in range(m):
        col_sum = 0
        for row in range(n):
            idx = row*m + col
            if i & (1 << idx) == 0:  # i & (1 << idx) == 0이면 세로로 더한다.
                col_sum = col_sum * 10 + arr[row][col]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum
    ans.append(total)

print(max(ans))
