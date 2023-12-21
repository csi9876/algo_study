import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque



def bfs(start):
    que = deque([start])
    v = [False for _ in range(n+1)]
    v[start] = True
    count = 1

    while que:
        next = que.popleft()
        for i in arr[next]:
            if v[i] == False:
                v[i] = True
                que.append(i)
                count += 1
    return count

n, m = map(int, input().split())
arr = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

res = [0 for _ in range(n+1)]

for i in range(1, n+1):
    res[i] = bfs(i)

maxn = max(res)
for i in range(1, n+1):
    if maxn == res[i]:
        print(i, end=' ')