import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
inf = sys.maxsize
adj = [[inf] * n for _ in range(n)]

for _ in range(m):
    s, e = map(int, input().split())
    adj[s-1][e-1] = 1
    adj[e-1][s-1] = 1

for i in range(n):
    adj[i][i] = 0

# 모든 정점 최소 거리, 플루이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

# 2개 선택해서 모두 방문 거리 측정
min_n = inf
res = []
for i in range(n):
    for j in range(i + 1, n):
        sum_n = 0
        for k in range(n):
            sum_n += min(adj[k][i], adj[k][j]) * 2
        if sum_n < min_n:
            min_n = sum_n
            res = [i + 1, j + 1, sum_n] # 1번 지점, 2번 지점, 총 거리
print(*res)