import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

s = min(arr)   # 최소 시간
e = max(arr) * m    # 최대 시간 * 인원
res = sys.maxsize

while s <= e:
    mid = (s + e) // 2
    cnt = 0  # mid 시간 동안 심사할 수 있는 최대 인원

    # 각 심사대에서 mid 시간동안 심사할 수 있는 사람 합
    for i in arr:
        cnt += mid // i

    # mid 시간 동안 심사할 수 있는 사람 수가 총 수 이상이면
    if cnt >= m:
        e = mid - 1
        res = min(res, mid)
    else:
        s = mid + 1

print(res)