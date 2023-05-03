import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(start):
    visited = [-1] * (N + 1)
    visited[start] = 0
    que = deque()
    que.append(start)
    while que:
        now = que.popleft()
        for e, w in adj[now]:
            if visited[e] == -1:
                que.append(e)
                visited[e] = visited[now] + w
    idx = max(visited)
    return [visited.index(idx),idx]

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e, w = map(int,input().split())
    adj[s].append([e,w])
    adj[e].append([s,w])
print(bfs(bfs(1)[0])[1])




