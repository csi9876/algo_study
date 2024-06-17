import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    adj = []
    cnt = 0
    for _ in range(m):
        a, b = map(int, input().split())
        adj.append((a, b))
    adj.sort(key=lambda x: (x[1], -x[0]))
    v = [0] * (n+1)

    for a, b in adj:
        for i in range(a, b+1):
            if not v[i]:
                cnt += 1
                v[i] = 1
                break
    print(cnt)
