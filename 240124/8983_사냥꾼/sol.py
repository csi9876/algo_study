import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from bisect import bisect_left

m, n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))

cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    # 동물이 사정거리 밖이면 넘어감
    if y > l:
        continue

    # 동물의 x 위치가 어느 사대인지 찾기
    nx = bisect_left(arr, x)

    # 찾은 위치와 이전 위치 확인
    for idx in (nx, nx - 1):
        # 인덱스 유효한 범위
        # 해당 사대와 동물의 거리가 사정거리 이내면 사냥
        if 0 <= idx < m:
            if abs(arr[idx] - x) + y <= l:
                cnt += 1
                break
print(cnt)