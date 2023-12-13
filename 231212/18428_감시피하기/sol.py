import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

import copy
from collections import deque
from itertools import combinations


N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]

blank = []
teachers = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            blank.append((i, j))
        if arr[i][j] == 'T':
            teachers.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS():
    que = deque([])
    for a, b in teachers:
        for i in range(4):
            que.append((a, b, i))
    while que:
        xx, yy, dd = que.popleft()
        nx = xx + dx[dd]
        ny = yy + dy[dd]
        if 0 <= nx < N and 0 <= ny < N:
            if temp[nx][ny] == 'S':
                return False
            elif temp[nx][ny] == 'X':
                que.append((nx, ny, dd))
    return True


for comb in combinations(blank, 3):
    temp = copy.deepcopy(arr)
    for x in comb:
        temp[x[0]][x[1]] = 'O'
    if BFS():
        print('YES')
        break
else:
    print('NO')