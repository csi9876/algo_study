import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    ab, bc, ca = map(int, input().split())

    res = 0

    # ab 0 ~ 최대
    for abNum in range(min(a, b) + 1):
        # bc 우선
        bcNum = min(b - abNum, c)   # min(b - ab갯수, c 갯수)
        caNum = min(c - bcNum, a - abNum)   # min(c - bc 갯수, a - ab 갯수)

        # 최대 이익
        res = max(res, abNum * ab + bcNum * bc + caNum * ca)

        # ca 우선
        caNum = min(c, a - abNum)
        bcNum = min(b - abNum, c - caNum)

        res = max(res, abNum * ab + bcNum * bc + caNum * ca)

    print(res)
