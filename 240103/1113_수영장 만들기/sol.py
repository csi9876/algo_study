import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
res = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# for i in range(n):
#     for j in range(m):
#         que = deque((j, i))
#
#         in

