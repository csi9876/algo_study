import sys
sys.stdin = open('input.txt')

import sys
import copy
input = sys.stdin.readline

# 2**N격자, 횟수
N, Q = map(int, input().split())
n = 2**N
arr = [list(map(int, input().split())) for _ in range(n)]
# 회전 반경 리스트
result = list(map(int, input().split()))
# print(result)

def check(arr):
    v = [[0]*(n) for _ in range(n)]
    # print(v)
    # temp = []
    for i in range(n):
        for j in range(n):

            if arr[i][j] > 0:
                if (i == 0 or i == n) and (j == 0 or j == n):
                    # temp.append((i,j))
                    v[i][j] = arr[i][j] - 1
                count = 0
                if i-1 >= 0 and arr[i-1][j] >0:
                    count += 1
                if i+1 < n and arr[i+1][j] >0:
                    count += 1
                if j-1 >= 0 and arr[i][j-1] >0:
                    count += 1
                if j+1 < n and arr[i][j+1] >0:
                    count += 1
                if count < 3:
                    v[i][j] = arr[i][j] - 1
                else:
                    v[i][j] = arr[i][j]
                if v[i][j] <= 0:
                    v[i][j] = 0
    return v

v = [[0]*(n) for _ in range(n)]
for l in result:
    l = 2**l
    for i in range(0, n, l):
        for j in range(0, n, l):
            for k in range(l):
                for l2 in range(l):
                    v[i+l2][j+l-k-1] = arr[i+k][j+l2]
                    arr[i+l2][j+l-k-1] = v[i+k][j+l2]

    arr = copy.deepcopy(v)
    arr = copy.deepcopy(check(arr))

# 남아있는 얼음의 합
result = 0
for i in arr:
    result += sum(i)
    # print(i)
print(result)

# print(arr)
# 얼음 중 가장 큰 덩어리가 차지하는 칸 개수
v = [[0]*(n) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxn = 0
for i in range(n):
    for j in range(n):
        count = 1
        if arr[i][j] != 0:
            que = [(i, j)]
            v[i][j] = 1
            while que:
                x, y = que.pop(0)
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny] != 0 and v[nx][ny] == 0:
                        v[nx][ny] = v[x][y]+1
                        que.append((nx,ny))
                        count += 1
        maxn = max(maxn, count)
# print(v)
if maxn > 1:
    print(maxn)
elif maxn <= 1:
    print(0)