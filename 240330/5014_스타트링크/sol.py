import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

# 전체, 시작, 목적, 위로, 아래로
f, s, g, u, d = map(int, input().split())

# 방문표시
visited = [False] * (f+1)

def bfs(start):
    que = deque([(start, 0)])
    visited[start] = True
    while que:
        cu, cnt = que.popleft() # 현재 층, cnt

        if cu == g:     # 목적층 도착
            return cnt

        # 위로 혹은 아래로 이동한 층을 확
        # 범위 내에 있고 방문하지 않은 경우 큐에 추가
        for next in (cu + u, cu - d):
            if 1 <= next <= f and not visited[next]:
                visited[next] = True
                que.append((next, cnt + 1))
    return "use the stairs"

print(bfs(s))