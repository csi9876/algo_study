import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

t = int(input())

def D(n):   # d 연산
    return (n * 2) % 10000

def S(n):   # s 연산
    return n - 1 if n != 0 else 9999

def L(n):   # l 연산
    return (n % 1000) * 10 + n // 1000

def R(n):   # r 연산
    return (n % 10) * 1000 + n // 10

def bfs(a, b):
    visited = [0] * 10000
    path = [''] * 10000
    que = deque([a])
    visited[a] = 1

    while que:
        n = que.popleft()

        for nxt, cmd in zip([D(n), S(n), L(n), R(n)], 'DSLR'):
            if not visited[nxt]:
                que.append(nxt)
                visited[nxt] = 1
                path[nxt] = path[n] + cmd

                if nxt == b:
                    que.clear()
                    break

    return path[b]

for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))