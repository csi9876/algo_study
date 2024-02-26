import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    cnt = 0     # 이동횟수
    idx = 1     # 이동 가능 거리
    sum_n = 0     # 이동 거리 합

    while sum_n < y - x:
        cnt += 1
        sum_n += idx    # cnt에 해당하는 idx 더하기
        if cnt % 2 == 0:    # cnt가 2의 배수이면
            idx += 1    # idx 증가
    print(cnt)

