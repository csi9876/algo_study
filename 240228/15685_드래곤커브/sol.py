import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * 101 for _ in range(101)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):
    y, x, d, g = map(int, sys.stdin.readline().split())
    arr[y][x] = 1   # 시작점에 드래곤 커브 표시
    dire = [d]
    # 세대만큼 반복
    for _ in range(g):
        # 이전 세대의 방향을 역순으로 90도 회전시켜서 dire 리스트에 추가
        for i in range(len(dire) - 1, -1, -1):
            dire.append((dire[i] + 1) % 4)

    # dire 리스트에 저장된 방향으로 드래곤 커브를 그림
    for i in range(len(dire)):
        y, x = y + dy[dire[i]], x + dx[dire[i]]
        arr[y][x] = 1

res = 0
for i in range(100):
    for j in range(100):
        # 네 꼭짓점이 모두 드래곤 커브인 정사각형이 있으면 res 값을 1 증가
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
            res += 1
print(res)


