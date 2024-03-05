import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)    # 진입 차수 초기화
graph = [[] for i in range(v + 1)]  # 연결 리스트

for _ in range(e):
    temp = list(map(int, input().split()))
    for i in range(len(temp)-2):
        graph[temp[i+1]].append(temp[i+2])
        indegree[temp[i+2]] += 1

result = []
q = deque()

for i in range(1, v + 1):   # 진입차수 0인 노드 큐에 삽입
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:    # 현재 노드와 연결된 노드들 진입차수 -1
        indegree[i] -= 1
        if indegree[i] == 0:    # 진입차수 0이면 큐에 삽입
            q.append(i)

if len(result) != v:    # 큐가 비면 사이클 존재
    print(0)
else:
    for i in result:
        print(i)
