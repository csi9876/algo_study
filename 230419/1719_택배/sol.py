import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

inf = int(1e9)
N, M = map(int, input().split())
adj = [[inf] * (N+1) for _ in range(N+1)]
v = [[0] * (N + 1) for _ in range(N + 1)]
# print(v)

for i in range(1, N+1):
    adj[i][i] = 0
    v[i][i] = '-'

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a][b] = min(adj[a][b], c)
    adj[b][a] = min(adj[b][a], c)
    v[a][b] = b
    v[b][a] = a

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
                v[i][j] = v[i][k]

for i in range(1, N+1):
    print(*v[i][1:])

