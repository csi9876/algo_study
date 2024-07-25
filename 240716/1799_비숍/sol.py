import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def check(idx):
    c = idx%2
    i, j = idx//n, idx%n
    dx, dy = [1, -1, 1, -1], [1, 1, -1, -1]

    for d in range(4):
        x, y = i+dx[d], j+dy[d]
        while 0<=x<n and 0<=y<n:
            if visited[x*n + y]:
                return False
            x += dx[d]
            y += dy[d]
    return True

def dfs(idx, c, cnt):
    if n*n-idx+1+cnt <= ans[c] or idx >= n*n:
        return

    ans[c] = max(ans[c], cnt)
    x, y = idx//n, idx%n
    j = y
    for i in range(x, n):
        while j < n:
            v = i*n + j
            if not visited[v] and arr[i][j] == 1 and check(v):
                visited[v] = 1
                dfs(v, c, cnt+1)
                visited[v] = 0
            j += 2
        j = (c+1)%2 if i%2 == 0 else c


visited = [0] * (n**2)
ans = [0, 0]

# 짝수는 0, 홀수는 1
dfs(0, 0, 0)
dfs(1, 1, 0)
print(sum(ans))