import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

def floyd_warshall(n, graph):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]




n, m = map(int, input().split())
graph = [[0] * (n + 1)] + \
        [[0] + list(map(int, input().split())) for _ in range(n)]

floyd_warshall(n, graph)

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")