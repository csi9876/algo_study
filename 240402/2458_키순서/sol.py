import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1

#플로이드 와샬 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] == 1 or (arr[i][k] == 1 and arr[k][j] == 1):
                arr[i][j] = 1  # 자신보다 작은 경우

res = 0
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        temp += arr[i][j] + arr[j][i]
    if temp == n-1:
        res += 1

print(res)