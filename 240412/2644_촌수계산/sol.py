import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
tx, ty = map(int, input().split())
m = int(input())
adj = [[] for _ in range(n+1)]
v = [0 for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

res = 0
que = deque([tx])   # tx에서 시작
v[tx] = 1

while que:
    for _ in range(len(que)):
        cur = que.popleft()  # 현 좌표
        if cur == ty:   # 목표와 동일하면 종료
            print(res)
            exit()
        for next in adj[cur]:   # 현좌표 인접행렬에서 que에 넣기
            if v[next] == 0:
                v[next] = 1
                que.append(next)
    res += 1

print(-1)
