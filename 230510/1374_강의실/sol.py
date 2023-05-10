import sys
sys.stdin = open('input.txt')

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
arr = [0] * (N)
for _ in range(N):
    a, s, e = map(int, input().split())
    arr[a-1] = (s, e)
# print(arr)
arr.sort()
# print(arr)

result = []
for i in range(N):
    s, e = heappop(arr)
    if len(result) == 0:
        heappush(result, (e, s))
        continue
    ne, ns = heappop(result)
    if ne > s:
        heappush(result, (ne, ns))
    heappush(result, (e, s))
print(len(result))


# cnt = 0
# s = arr[0][0]
# for i in range(N):
#     if arr[i][1] < s:
#         cnt += 1
#         s = arr[i][0]
# print(cnt)


