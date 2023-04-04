import sys
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]
# print(adj)
for _ in range(1, N):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
# print(adj)

q = int(input())
for _ in range(q):
    k, t = map(int, input().split())
    if k == 1:
        if len(adj[t]) == 1:
            print('no')
        else:
            print('yes')
    elif k == 2:
        print('yes')