import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque


n, k = map(int, input().split())
m = len(str(n))

v = set()
v.add((n, 0))   # 방문 숫자, 변경 횟수
que = deque([(n, 0)])
res = -1

while que:
    x, cnt = que.popleft()
    if cnt == k:
        res = max(res, x)
        continue
    x = list(str(x))
    for i in range(m-1):
        for j in range(i+1, m):
            if i == 0 and x[j] == "0":
                continue
            x[i], x[j] = x[j], x[i]
            temp = int(''.join(x))
            if (temp, cnt+1) not in v:
                que.append((temp, cnt+1))
                v.add((temp, cnt+1))
            x[i], x[j] = x[j], x[i]


print(res)
