import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

# 벨만 포드
def bellman_ford(start, n):
    # 정점까지의 거리 초기값
    dist = [int(1e9) for _ in range(n + 1)]
    dist[start] = 0  # 시작점은 0
    for i in range(n):
        for s, e, t in adj:
            # 현재 간선을 통해 다른 정점으로 이동하는 거리가 더 짧으면
            if dist[e] > dist[s] + t:
                # n-1 라운드에서도 값이 갱신되면 음수 사이클 존재
                if i == n - 1:
                    return True
                dist[e] = dist[s] + t
    # 음수 사이클이 없는 경우
    return False

t = int(input())
for _ in range(t):
    n, m, w = map(int, input().split())
    adj = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        adj.append((s, e, t))
        adj.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        adj.append((s, e, -t))





    res = bellman_ford(1,n)
    if res == 1:
        print("YES")
    else:
        print("NO")