import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
# 구름 이동
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 바구니
cx = [-1, 1, -1, 1]
cy = [1, 1, -1, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
mrr = [list(map(int, input().split()))for _ in range(M)]
# print(arr)
# print(mrr)
ccc = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
for i in mrr:
    temp = set()
    for j in range(len(ccc)):
        x, y = ccc.pop()
        nx = (x + dx[i[0]-1]*i[1])%N
        ny = (y+dy[i[0]-1]*i[1])%N
        arr[nx][ny] += 1
        temp.add((nx,ny))

    while temp:
        x, y = temp.pop()
        count = 0
        for k in range(4):
            nx = x+cx[k]
            ny = y+cy[k]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny]:
                count += 1
        arr[x][y] += count

    # for x, y in temp:
    #     count = 0
    #     for k in range(4):
    #         nx = x+cx[k]
    #         ny = y+cy[k]
    #         if 0<=nx<N and 0<=ny<N and arr[nx][ny]:
    #             count += 1
    #     arr[x][y] += count
    for k in range(N):
        for l in range(N):
            if arr[k][l] >= 2 and (k, l) not in temp:
                arr[k][l] -= 2
                ccc.append((k,l))

result = 0
for i in arr:
    result += sum(i)
print(result)