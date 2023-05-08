import sys
sys.stdin = open('input.txt')

# dp[i][j] : (1,1) > (i,j) 까지의 경로 개수
# 네 방향으로부터 범위 내 0<=x<N / 0<=y<M
# i,j보다 ni,nj가 더 작아야 한다

def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx, ny = x+dx, y+dy
            if arr[nx][ny] > arr[x][y]:
                dp[x][y] += dfs(nx,ny)
    return dp[x][y]





N, M = map(int, input().split())
arr = [[0]*(M+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]
# print(arr)
dp = [[-1]*(M+2) for _ in range(N+2)]
dp[1][1] = 1

print(dfs(N,M))