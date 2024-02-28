import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n, c = map(int, input().rstrip().split())
m = int(input())

adj = []
for _ in range(m):
    s, e, v = map(int, input().split())
    adj.append((s, e, v))
adj.sort(key=lambda x : x[1])
res = 0
limit = [c] * (n + 1)   # 마을 별 한계

for i in range(m):
    temp = c
    for j in range(adj[i][0], adj[i][1]):   # 출발 ~ 도착
        temp = min(temp, limit[j])  # 옮길 수 있는 것 vs 상한
    temp = min(temp, adj[i][2])     # 옮길 수 있는 것 vs 실제 박스

    for k in range(adj[i][0], adj[i][1]):
        limit[k] -= temp    # 옮긴 것은 뺀다
    res += temp

print(res)