import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

in_degree = [0] * (n + 1)     # 진입차수
in_degree[0] = -1
dire = [[] for _ in range(n + 1)]
que = deque()

for _ in range(m):
    a, b = map(int, input().split())
    in_degree[b] += 1   # 키가 더 크면 더 많이 비교, 진입 차수 증가
    dire[a].append(b)   # 차수 확인을 위한 lst

for i in range(1, n + 1):   # 진입차수 0 큐로 제외
    if in_degree[i] == 0:
        que.append(i)

res = []
while que:
    cx = que.popleft()
    res.append(cx)
    for k in dire[cx]:
        in_degree[k] -= 1
        if in_degree[k] == 0:
            que.append(k)

print(*res)