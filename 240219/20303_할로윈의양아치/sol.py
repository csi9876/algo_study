import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
v = [0] * n

# 친구들 그룹 묶기
def group(c):
    fri = 1     # 친구 수
    candy = arr[c]  # 사탕 수
    que = deque()
    que.append(c)
    v[c] = 1
    while que:
        nc = que.popleft()
        for i in adj[nc]:
            if v[i] == 0:
                que.append(i)
                v[i] = 1
                fri += 1
                candy += arr[i]
    return [fri, candy]

group_candy= []     # [그룹 아이 수, 그룹 사탕 수]
for i in range(n):
    if v[i] == 0:   # 방문하지 않은 노드는 그룹화
        group_candy.append(group(i))

dp = [0 for _ in range(k + 1)]
for i in range(len(group_candy)):
    child_cnt, candy_cnt = group_candy[i]
    # 현재 그룹의 아이 수부터 총 아이들 수가지 역으로 탐색
    for j in range(k, child_cnt - 1, -1):
        # 현재 아이 수에 해당하는 사탕 수 vs 이전 사탕 수
        dp[j] = max(dp[j - child_cnt] + candy_cnt, dp[j])

print(dp[k - 1])