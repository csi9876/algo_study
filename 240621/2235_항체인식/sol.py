import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque


n, m = map(int, input().split())
before = [list(map(int, input().split())) for _ in range(n)]
after = [list(map(int, input().split())) for _ in range(n)]

# BFS 함수 정의
def bfs(x, y, num, before):
    n = len(before)
    m = len(before[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit = [[False for _ in range(m)] for _ in range(n)]
    temp = before[x][y]

    q = deque()
    q.append((x, y))
    visit[x][y] = True

    while q:
        x, y = q.popleft()
        before[x][y] = num

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not (0 <= nx < n and 0 <= ny < m):  # 범위를 벗어나면 무시
                continue
            if not visit[nx][ny] and before[nx][ny] == temp:  # 방문하지 않았고 값이 같다면
                q.append((nx, ny))
                visit[nx][ny] = True


def solution(n, m, before, after):
    for i in range(n):
        for j in range(m):
            if before[i][j] != after[i][j]:  # 값이 다르면 BFS로 변경
                bfs(i, j, after[i][j], before)
                # 변경 후 행렬과 비교
                for r in range(n):
                    for c in range(m):
                        if before[r][c] != after[r][c]:  # 값이 다르면 "NO" 반환
                            return "NO"
                return "YES"  # 모든 값이 같다면 "YES" 반환
    return "YES"  # 처음부터 모든 값이 같다면 "YES" 반환

print(solution(n, m, before, after))  # 결과 출력