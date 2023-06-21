import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
name = []
for _ in range(N):
    na = int(input())
    name.append(na)
print(name)
temp = M
res = 0

# def check(t, e, arr):
#     while arr:
#         i = arr[0]
#         if t >= i:
#             t -= i + 1
#             arr.pop(0)
#             check(M, e+(t+1)*(t+1), arr)
#
#         else:
#             e += (t + 1) * (t + 1)
#             t = M
#
#         if t == 0:
#             e += 1
#             t = M
#
#         if t == -1:
#             e += 0
#             t = M
#
#     return res
# print(check(M, 0, name))

while name:
    i = name[0]
    if temp >= i:
        temp -= i+1
        name.pop(0)

    else:
        res += (temp+1) * (temp+1)
        temp = M

    if temp == 0:
        res += 1
        temp = M

    if temp == -1:
        res += 0
        temp = M

print(res)

