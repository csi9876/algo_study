import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque
sys.setrecursionlimit(10 ** 9)

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
cycle = set()   # 사이클 판별 set
v = [0] * (n + 1)

res = 0

def dfs(start, here, level, li):
    global res
    if level <= 2:
        for i in adj[here]:
            if v[i] == 0:
                v[i] = 1
                dfs(start, i, level+1, li+[i])
                v[i] = 0
    else:
        for i in adj[here]:
            if v[i] == 0:
                v[i] = 1
                dfs(start, i, level+1, li+[i])
                v[i] = 0
            else:
                if i == start:
                    res = 1
                    for l in li:
                        cycle.add(l)
                    return
# dfs 수행
for i in range(1, n+1):
    if res == 1:
        break
    v[i] = 1
    dfs(i, i, 1, [i])
    v[i] = 0

# bfs 수행
answer = [int(1e9)] * (n + 1)
que = deque()
for c in cycle:
    que.append((c, 0))
    answer[c] = 0

while que:
    node, level = que.popleft()

    for i in adj[node]:
        if answer[i] == int(1e9):
            answer[i] = level+1
            que.append((i, level+1))


print(" ".join(map(str, answer[1:])))