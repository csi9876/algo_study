import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, count):
    global result
    result = max(result, count)

    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<R and 0<=ny<C and v[ord(arr[nx][ny])] == 0:
            v[ord(arr[nx][ny])] = 1
            dfs(nx, ny, count+1)
            v[ord(arr[nx][ny])] = 0

R, C = map(int, input().split())
arr = list(input() for _ in range(R))

result = 0
v = [0] * 128
v[ord(arr[0][0])] = 1
dfs(0,0,1)
print(result)