import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
adj = [[0] * (N+1) for _ in range(N+1)]
# print(arr)
# print(adj)
for _ in range(M):
    s, e = map(int, input().split())
    adj[s][e] = 1
    adj[e][s] = 2
# print(adj)
for _ in range(2):
    for i in range(N+1):
        adj[i][i] = 3
        for j in range(N+1):
            if adj[i][j] == 1:
                for k in range(N+1):
                    if adj[j][k] == 1:
                        adj[i][k] = 1

            if adj[i][j] == 2:
                for k in range(N+1):
                    if adj[j][k] == 2:
                        adj[i][k] = 2
# print(adj)

for i in adj[1:]:
    count = 0
    for j in i[1:]:
        if j == 0:
            count += 1
    print(count)

# print(arr)
# for i in range(len(arr)):
#     if len(arr[i]) >= 1:
#         for j in arr[i]:
#             # print(j)
#             # print(arr[j])
#             if arr[j] != []:
#                 arr[i].append(*arr[j])
# print(arr)