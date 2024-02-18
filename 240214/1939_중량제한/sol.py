import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
    adj[b].append([a, c])

a, b = map(int, input().split())

s = 1
e = sys.maxsize

res = 0

# 현재 값 이상의 가중치를 가진 경로 있는지 탐색
def solve(mid):
    que = deque()
    que.append(a)
    v = [0] * (n+1)
    v[a] = 1

    while que:
        x = que.popleft()

        # 연결 노드 순회
        for i, w in adj[x]:
            # 연결 노드를 방문하지 않았고 가중치가 mid 이상이면 que
            if not v[i] and w >= mid:
                v[i] = 1
                que.append(i)
    # 끝 노드를 방문했다면 1 반환
    if v[b]:
        return 1
    else:
        return 0

while s <= e:
    mid = (s + e) // 2
    if solve(mid):
        res = mid
        s = mid + 1
    else:
        e = mid - 1

print(res)