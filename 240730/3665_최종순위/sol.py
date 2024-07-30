import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline


n = int(input())
arr = []
for i in range(n):
    d, t = map(int, input().split())
    # 시작해야 하는 날, 걸리는 기간, 마감 기한
    arr.append((t - d + 1, d, t))

arr.sort(key=lambda x: (-x[2], -x[1]))

# 첫 번째 과제 시작일
res = arr[0][0]

for i in range(1, n):
    start, mid, end = arr[i]
    # 현재 과제의 시작일이 이전 과제 종료일보다 늦다면
    # 현재 과제 시작일을 변경
    if res > end:
        res = start
    else:
        # 현재 과제 시작일이 빠르면
        # 현재 과제 시작일 = 이전 과제 시작일 - 현재 과제 걸리는 기간
        res = res - mid

print(res - 1)