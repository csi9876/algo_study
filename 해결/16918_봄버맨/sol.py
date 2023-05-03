import sys
sys.stdin = open('input.txt')

from collections import deque
# import sys
# input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

r, c, n = map(int, input().split())
arr = [list(input())for _ in range(r)]

def bfs(que):
    while que:
        x, y = que.popleft()
        arr[x][y] = '.'
        for l in range(4):
            ny = dy[l] + y
            nx = dx[l] + x
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == 'O':
                arr[nx][ny] = '.'
                # queue.append((yy, xx)) 연쇄반응이 없다.

def search(q): # 폭탄 탐색
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                q.append((i, j))

que = deque()

if n == 1:
    for lst in arr:
        print(*lst, sep='')

else:
    search(que) # for문 돌기전에 폭탄 탐색
    for k in range(1,n):
        # 짝수면 전부 폭탄으로 만들기
        if (k+1) % 2 == 0: # for문돌면서 . -> O으로 바꿔야함
            for i in range(r):
                for j in range(c):
                    if arr[i][j] == '.':
                        arr[i][j] = 'O'
            if (k+1) == n: # 결과출력
                for lst in arr:
                    print(*lst, sep='')
        else:
            # 홀수면 폭탄 터트리기
            bfs(que)
            # 이후 폭탄 탐색
            search(que)
            if (k+1) == n: # 결과출력
                for lst in arr:
                    print(*lst, sep='')