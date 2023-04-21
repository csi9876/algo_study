
"""
ANS => n개의 줄을 출력
 i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용
---------------------------------------------------------------------------
- 다익스트라: 한 지점에서 다른 모든 지점까지의 최단 경로를 계산하는 알고리즘
- 플로이드 워셜: 모든 지점에서 다른 모든 지점까지의 최단 경로를 계산하는 알고리즘
<플로이드–워셜>
다음과 같이 3중 반복문을 이용해 구현할 수 있다.
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])
"""

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

inf = int(1e9)
N = int(input())
M = int(input())
adj = [[inf] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    adj[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a][b] = min(adj[a][b], c)

# 플로이드 워셜
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if adj[i][j] == inf:
            adj[i][j] = 0

for i in range(1, N+1):
    print(*adj[i][1:])