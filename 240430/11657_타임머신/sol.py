import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

inf = sys.maxsize
v = [inf] * (n+1)

def belman_ford(start):
    v[start] = 0
    for i in range(1, n+1):
        for now in range(1, n+1):
            for next, weight in adj[now]:
                if v[now] != inf and v[next] > v[now] + weight:
                    v[next] = v[now] + weight
                    if i == n:
                        if v[next] > v[now] + weight:
                            return True
    return False

if belman_ford(1):
    print(-1)
else:
    for i in range(2, n+1):
        if v[i] == inf:
            print(-1)
        else:
            print(v[i])