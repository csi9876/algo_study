import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

for i in range(1, int(input())+1):
    w1, w2, w3 = input().split()
    idx = 0
    que = deque([(0, 0)])
    visited = [[0] * (len(w2) + 1) for _ in range(len(w1) + 1)]
    while que:
        for _ in range(len(que)):
            a, b = que.popleft()
            if a < len(w1) and not visited[a + 1][b] and w1[a] == w3[idx]:
                visited[a + 1][b] = 1
                que.append((a + 1, b))
            if b < len(w2) and not visited[a][b + 1] and w2[b] == w3[idx]:
                visited[a][b + 1] = 1
                que.append((a, b + 1))
        idx += 1
    res = 'yes' if idx == len(w3) + 1 else 'no'
    print(f'Data set {i}: {res}')