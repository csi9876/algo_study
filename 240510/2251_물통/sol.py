import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

def bfs(a, b, c):
    queue = deque([(0, 0, c)])  # 초기 상태
    visited = set()     # 방문
    result = set()      # 결과

    while queue:
        x, y, z = queue.popleft()
        if (x, y, z) in visited:    # 이미 방문했으면 패스
            continue
        visited.add((x, y, z))

        if x == 0:  # a 물통이 비어 있으면 결과에 추가
            result.add(z)

        # 6가지 경우 모두 큐에 추가
        # A -> B
        nx, ny = max(0, x - (b - y)), min(b, y + x)
        queue.append((nx, ny, z))
        # A -> C
        nx, nz = max(0, x - (c - z)), min(c, z + x)
        queue.append((nx, y, nz))
        # B -> A
        nx, ny = min(a, x + y), max(0, y - (a - x))
        queue.append((nx, ny, z))
        # B -> C
        ny, nz = max(0, y - (c - z)), min(c, z + y)
        queue.append((x, ny, nz))
        # C -> A
        nx, nz = min(a, x + z), max(0, z - (a - x))
        queue.append((nx, y, nz))
        # C -> B
        ny, nz = min(b, y + z), max(0, z - (b - y))
        queue.append((x, ny, nz))

    return sorted(list(result))

a, b, c = map(int, input().split())
res = bfs(a, b, c)

print(*res)