import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

# 길이, 높이(구간 나누는)
N, H = map(int, input().split())

# 석순 종유석 번갈아
# 파괴하는 장애물의 최소값과 구간 수

u = []
d = []
for i in range(N):
    a = int(input())
    if i%2 == 0:
        d.append(a)
    else:
        u.append(a)

u.sort()
d.sort()
# print(d)
# print(u, d)
result = [int(1e9)] * (H+1)
for i in range(1, H+1):
    temp = 0
    dd = bisect_left(d, i)
    temp += len(d)-dd
    uu = bisect_right(u, H-i)
    temp += len(u)-uu

    result[i] = temp
# print(result)

print(min(result), result.count(min(result)))