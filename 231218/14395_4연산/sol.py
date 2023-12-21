import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque


s, t = map(int, input().split())
v = set()

if s == t:
    print(0)
else:
    v.add(s)
    que = deque()
    que.append((s, ''))

    flag = 0
    while que:
        temp, res = que.popleft()

        if temp == t:
            print(res)
            flag = 1
            break

        for i in ("*", "+", "/"):
            if i == "*":
                new = temp*temp
            elif i == "+":
                new = temp+temp
            else:
                new = 1

            if 0 <= new <= t and new not in v:
                v.add(new)
                que.append((new, res + i))
    if flag == 0:
        print(-1)