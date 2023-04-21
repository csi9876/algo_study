import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline
#
inf = int(1e9)
N = int(input())
M = int(input())
adj = [[inf] * (N+1) for _ in range(N+1)]
v=[[[0] for _ in range(N+1)] for _ in range(N+1)]
# print(v)
for i in range(1, N+1):
    adj[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a][b] = min(adj[a][b], c)
    v[a][b] = [a, b]
    v[b][a] = [b, a]
# print(v)
# 플로이드 워셜
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
                v[i][j] = [*v[i][k], k, *v[k][j]]


for i in range(1, N+1):
    print(*adj[i][1:])
for j in range(1,N+1):
    for k in range(1, N+1):
        temp = []
        for ans in v[j][k]:
            if ans not in temp:
                temp.append(ans)
        if len(temp) == 1:
            print(0)
        else:
            print(len(temp), *temp)

# import sys
# input = sys.stdin.readline
#
# # 도시
# n = int(input())
# # 버스의 개수
# m = int(input())
#
# INF = int(1e9)
# graph = [[INF]*(n+1) for _ in range(n+1)]
# road = [[0]*(n+1) for _ in range(n+1)]
#
# for i in range(n+1):
#     graph[i][i] = 0
#
# # 버스의정보
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = min(c, graph[a][b])
#
# # 최소비용
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         for k in range(1, n+1):
#             if graph[j][k] > graph[j][i] + graph[i][k]:
#                 graph[j][k] = graph[j][i] + graph[i][k]
#                 road[j][k] = i
#             else:
#                 continue
#             # graph[j][k] = min(graph[j][i]+ graph[i][k], graph[j][k])
#
# # 최소비용
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == INF:
#             print(0, end=' ')
#         else:
#             print(graph[i][j], end=' ')
#     print()
#
# # i * n + j 번째 줄에는 도시 i에서 도시 j로 가는 최소비용에 포함되어 있는
# # 도시의 개수 k
# # 도시 i에서 도시 j로 가는 경로
#
# # i와 j 표시
# for i in road[1:]:
#     print(i[1:])
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i!= j and not road[i][j]:
#             road[i][j] = j
#
# for i in road[1:]:
#     print(i[1:])
#
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i==j:
#             print(0)
#
#         else:
#             if road[i][j] == j:
#                 print(2, i, j)
#             else:
#                 # 다 담아
#                 way = []
#                 # 도착지 담기
#                 way.append(j)
#
#                 # 맨마지막 방문한곳
#                 q = []
#                 q.append(road[i][j])
#
#                 while q:
#                     mom = q.pop()
#                     way.append(mom)
#
#                     if road[i][mom] != mom:
#                         q.append(road[i][mom])
#                     else:
#                         # way.append(mom)
#                         break
#
#                 # 출발지 담기
#                 way.append(i)
#                 print(len(way), *way[::-1])