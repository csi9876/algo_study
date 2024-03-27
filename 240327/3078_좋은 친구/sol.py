import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
arr = []

for i in range(1, n + 1):
    a = input().strip()
    a = len(a)
    arr.append((i, a))

res = 0
que = [deque() for _ in range(21)]  # 이름 길이 별로 등수 저장

for idx, l in arr:
    # 큐가 있고, 등수 차이가 k보다 크면 계속 제거
    while que[l] and idx - que[l][0] > k:
        que[l].popleft()

    # 같은 큐는 좋은 친구
    if que[l]:
        res += len(que[l])
    que[l].append(idx)

print(res)

