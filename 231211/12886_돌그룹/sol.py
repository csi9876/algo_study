import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

a, b, c = map(int, input().split())
n = a+b+c
v = [[0] * (n+1) for _ in range(n+1)]

# 합이 3이 아니면 동일한 3그룹 안 나옴
if n % 3 != 0:
    print(0)
else:
    que = deque()
    que.append((a, b))  # 두 그룹을 que에 넣기
    v[a][b] = 1     # 방문 표시

    while que:
        x, y = que.popleft()
        z = n - x - y   # 3번째 그룹의 갯수
        if x == y == z:     # 3 그룹 동일하면 1 출력하고 종료
            print(1)
            break

        # 두 그룹 간 돌 갯수 비교
        for nx, ny in (x, y), (y, z), (x, z):
            if nx < ny:     # 크거나 작으면 돌 갯수 변경
                ny -= nx
                nx += nx
            elif nx > ny:
                nx -= ny
                ny += ny
            else:       # 같으면 넘기기
                continue
            nz = n - nx - ny    # 돌 변경 후 남은 그룹 갯수
            x = min(nx, ny, nz)     # 가장 작은 그룹
            y = max(nx, ny, nz)     # 가장 큰 그룹

            if not v[x][y]:     # 아직 분배한 적 없던 조합이면
                que.append((x, y))      # 분배 실시
                v[x][y] = 1     # 방문 표시
    else:
        print(0)


