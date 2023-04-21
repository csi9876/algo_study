import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

inf = int(1e9)
N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
print(adj)

# 플로이드 워셜
for k in range(N):
    for i in range(N):
        for j in range(N):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

for i in range(N):
    print(*adj[i])