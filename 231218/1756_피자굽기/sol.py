import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n, m = map(int, input().split())

adj = [[] for _ in range(n)]
v = [0] * n
res = 0
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)


def dfs(cnt, x):
    global res
    if cnt == 4:
        res = 1
        return
    for j in adj[x]:
        if not v[j]:
            v[j] = 1
            dfs(cnt + 1, j)
            v[j] = 0


for i in range(n):
    v[i] = 1
    dfs(0, i)
    v[i] = 0
    if res:
        print(1)
        break
else:
    print(0)