

import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
que = []
for _ in range(N):
    x = -int(input())

    # print(x)
    if x == 0:
        try:
            print(-heappop(que))
        except:
            print(0)
    else:
        heappush(que, x)

