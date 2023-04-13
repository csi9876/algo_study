import sys
sys.stdin = open('input.txt')

# import sys
# input = sys.stdin.readline
# from heapq import heappop, heappush
#
# V, E = map(int, input().split())
# arr = [[]for _ in range(V+1)]
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     arr[a].append((c, b))
#     arr[b].append((c, a))
# # print(arr)
# x, y = map(int, input().split())
# # print(x, y)
# que = []
#
# def ik(start, end):
#     v = [float('inf')] * (V+1)
#     v[start] = 0
#     heappush(que, (0, start))
#     while que:
#         dist, now = heappop(que)
#         if dist > v[now]:
#             continue
#
#         for toNode, toDist in arr[now]:
#             d = dist + toDist
#             if v[toNode] > d:
#                 v[toNode] = d
#                 heappush(que, (d, toNode))
#
#     return (v[0] + v[end], v[V - 1])
#
#
# # 다익스트라로 만들 수 있는 경로 조합 생성
# one_v1_v2, v1_end = ik(x, y)
# one_v2_v1, v2_end = ik(y, x)
#
# # v1, v2 각각의 정점을 먼저 거치는 두 가지 경로의 최소값 도출
# r = min(one_v1_v2 + v2_end, one_v2_v1 + v1_end)
# print(r if r != float('inf') else -1)
#
# import heapq
# import sys
#
# input = sys.stdin.readline
#
# n, e = map(int, input().split())
# heap = []
#
# # 인접 리스트 생성 및 할당
# linked = [[] for i in range(n)]
# for i in range(e):
#     a, b, c = map(int, input().split())
#     linked[a - 1].append((b - 1, c))
#     linked[b - 1].append((a - 1, c))
#
# v1, v2 = map(int, input().split())
# v1 -= 1;
# v2 -= 1
#
#
# def djikstra(start, end):
#     dist = [float('inf')] * n
#     dist[start] = 0
#     heapq.heappush(heap, (0, start))
#     while (heap):
#         curDist, curNode = heapq.heappop(heap)
#         if curDist > dist[curNode]:
#             continue
#
#         for toNode, toDist in linked[curNode]:
#             d = curDist + toDist
#             if dist[toNode] > d:
#                 dist[toNode] = d
#                 heapq.heappush(heap, (d, toNode))
#
#     return (dist[0] + dist[end], dist[n - 1])
#
#
# # 다익스트라로 만들 수 있는 경로 조합 생성
# one_v1_v2, v1_end = djikstra(v1, v2)
# one_v2_v1, v2_end = djikstra(v2, v1)
#
# # v1, v2 각각의 정점을 먼저 거치는 두 가지 경로의 최소값 도출
# r = min(one_v1_v2 + v2_end, one_v2_v1 + v1_end)
# print(r if r != float('inf') else -1)


#
# def ik(cost, start):
#     que = []
#     heappush(que,(cost, start))
#
#     while que:
#         cost, start = heappop(que)
#         if v[start] < cost:
#             continue
#         for cc, dd in arr[start]:
#             res = cost + cc
#             if res < v[dd]:
#                 v[dd] = res
#                 heappush(que, (res, dd))
#             if dd == x:
#                 return v[dd]
#
# def ik1(cost, start):
#     que = []
#     heappush(que,(cost, start))
#
#     while que:
#         cost, start = heappop(que)
#         if v[start] < cost:
#             continue
#         for cc, dd in arr[start]:
#             res = cost + cc
#             if res < v[dd]:
#                 v[dd] = res
#                 heappush(que, (res, dd))
#             if dd == y:
#                 return v[dd]
#
# def ik2(cost, start):
#     que = []
#     heappush(que, (cost, start))
#
#     while que:
#         cost, start = heappop(que)
#         if v[start] < cost:
#             continue
#         for cc, dd in arr[start]:
#             res = cost + cc
#             if res < v[dd]:
#                 v[dd] = res
#                 heappush(que, (res, dd))
#     return v[-1]
#
#
#
# try:
#     result = []
#     if x==1 and y == V:
#         v = [int(1e9)] * (V + 1)
#         # v[x] = 0
#         result.append((ik2(0, x)))
#         print(sum(result))
#
#     elif x==1 and y != V:
#         v = [int(1e9)] * (V + 1)
#         # v[x] = 0
#         result.append((ik1(0, x)))
#         v = [int(1e9)] * (V + 1)
#         # v[y] = 0
#         result.append((ik2(0, y)))
#         # print(result)
#         print(sum(result))
#
#     elif x!=1 and y==V:
#         v = [int(1e9)] * (V + 1)
#         # v[x] = 0
#         result.append((ik1(0, 1)))
#         v = [int(1e9)] * (V + 1)
#         # v[y] = 0
#         result.append((ik2(0, x)))
#         print(sum(result))
#
#     else:
#         v = [int(1e9)] * (V+1)
#         # v[1] = 0
#         result.append((ik(0,1)))
#         v = [int(1e9)] * (V+1)
#         # v[x] = 0
#         result.append((ik1(0,x)))
#         v = [int(1e9)] * (V+1)
#         # v[y] = 0
#         result.append((ik2(0,y)))
#         # print(result)
#
#
#         result1 = []
#         v = [int(1e9)] * (V+1)
#         # v[1] = 0
#         result1.append((ik1(0,1)))
#         v = [int(1e9)] * (V+1)
#         # v[y] = 0
#         result1.append((ik(0,y)))
#         v = [int(1e9)] * (V+1)
#         # v[x] = 0
#         result1.append((ik2(0,x)))
#         # print(result1)
#
#         if int(1e9) in result1 or result:
#             print(-1)
#         else:
#             print(min(sum(result), sum(result1)))
# except:
#     print(-1)

# from heapq import heappop, heappush
# import sys
# # input = sys.stdin.readline
# sys.stdin = open('input.txt')
# 
# v, e = map(int, input().split())
# graph = [[] for _ in range(v+1)]
# visited = [int(1e9)] * (v+1)
# 
# for _ in range(e):
#     start, end, cost = map(int, input().split())
#     graph[start].append((cost, end))
#     graph[end].append((cost,start))
# 
# def dijkstra(start):
#     q = []
#     heappush(q, (0, start))
#     visited[start] = 0
#     while q:
#         cost, now = heappop(q)
#         if visited[now] < cost:
#             continue
#         for i in graph[now]:
#             res = cost + i[0]
#             if res < visited[i[1]]:
#                 visited[i[1]] = res
#                 heappush(q, (res, i[1]))
#     return visited
# 
# v1, v2 = map(int, input().split())
# 
# one = dijkstra(1)
# print(one)
# v1_dis = dijkstra(v1)
# print(v1_dis)
# v2_dis = dijkstra(v2)
# print(v2_dis)
# 
# v1_path = one[v1] + v1_dis[v2] + v2_dis[v]
# print(v1_path)
# v2_path = one[v2] + v1_dis[v1] + v1_dis[v]
# print(v2_path)
# result = min(v1_path, v2_path)
# if result <= int(1e9):
#     print(result)
# else:
#     print(-1)

import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush


def dijkstra(go):
    global result1, result2
    heap = []
    heappush(heap, go)
    while heap:
        cost, now = heappop(heap)
        if visited[now] < cost:
            continue
        for check in edge[now]:
            total = cost + check[0]
            if total < visited[check[1]]:
                visited[check[1]] = total
                heappush(heap, [total, check[1]])
    if go[1] == 1:
        result1 += visited[exam_node1]
        result2 += visited[exam_node2]
        return
    if go[1] == exam_node1:
        result1 += visited[exam_node2]
        result2 += visited[N]
        return
    if go[1] == exam_node2:
        result1 += visited[N]
        result2 += visited[exam_node1]


N, E = map(int, input().split())

edge = [[] for _ in range(N+1)]
visited = [int(1e9)] * (N+1)
for node in range(E):
    start, end, distance = map(int, input().split())
    edge[start].append([distance, end])
    edge[end].append([distance, start])

exam_node1, exam_node2 = map(int, input().split())

result1 = 0
result2 = 0

dijkstra([0, 1])
dijkstra([0, exam_node1])
dijkstra([0, exam_node2])

if result1 >= int(1e9) or result2 >= int(1e9):
    print(-1)
else:
    print(min(result1, result2))