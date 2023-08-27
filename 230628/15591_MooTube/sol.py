import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque

N, Q = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = (map(int, input().split()))
    arr[p].append((r, q))
    arr[q].append((r, p))
# print(arr)

for _ in range(Q):
    # 상한 유사도 / 동영상 번호
    K, V = map(int, input().split())
    # print(K, V)
    visited = [0] * (N + 1)
    visited[V] = 1
    res = 0
    que = deque([(V, int(1e9))])
    # que = [(V, int(1e9))]

    while que:
        v, r = que.popleft()
        for nr, nv in arr[v]:
            # print(nr, nv)
            nr = min(r, nr)

            if nr >= K and not visited[nv]:
                res += 1
                que.append((nv, nr))
                visited[nv] = 1
    print(res)
