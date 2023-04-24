import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    que = []
    v = [0] * n

    que.append((x, y))

    while que:
        x, y = que.pop(0)
        if abs(x-ex) + abs(y-ey) <= 1000:
            return 'happy'

        for i in range(n):
            if v[i] == 0:
                nx, ny = arr[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    que.append((nx,ny))
                    v[i] = 1
    return 'sad'


t = int(input())
for tc in range(t):
    n = int(input())
    x, y = map(int, input().split())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a,b))

    ex, ey = map(int, input().split())

    result = bfs(x, y)
    print(result)