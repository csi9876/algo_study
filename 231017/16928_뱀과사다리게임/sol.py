import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
v = [0 for _ in range(101)]
arr = []
snake = []

for i in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])

for i in range(M):
    s, e = map(int, input().split())
    snake.append([s, e])

que = deque()
que.append([1, 0])
v[1] = 1

while que:
    temp, count = que.popleft()

    if temp == 100:
        print(count)
        break

    for i in range(1, 7):
        newtemp = temp + i
        if newtemp > 100:
            continue

        for k in range(len(arr)):
            if newtemp == arr[k][0] and not v[newtemp]:
                v[newtemp] = True
                que.append([arr[k][1], count + 1])

        for j in range(len(snake)):
            if newtemp == snake[j][0] and not v[newtemp]:
                v[newtemp] = True
                que.append([snake[j][1], count + 1])

        if not v[newtemp]:
            v[newtemp] = True
            que.append([newtemp, count + 1])
