import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[10] * (N+1) for _ in range(N+1)]
print(adj)
for _ in range(M+1):
    s, e, w = map(int, input().split())
    adj[s][e] = w
print(adj)