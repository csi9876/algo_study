import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


N, L = map(int, input().split())
arr = []
for i in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key=lambda x: (x[0], x[1]))

temp = arr[0][0]
count = 0

for now, next in zip(arr, arr[1:]):
    s, e = now
    w = e-temp
    div = w//L
    if w % L != 0:
        div += 1
    count += div
    temp = max(temp + div * L, next[0])

w = arr[-1][1] - max(temp, arr[-1][0])
if (w >= 0):
    div = w // L
    if (w % L != 0):
        div += 1
    count += div
print(count)

'''
123456 7 89101112 1314151617
3 3       3          3  3
6 5 5

'''