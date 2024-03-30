import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = sorted(list(int(input()) for _ in range(k)), reverse=True)

s = 1
e = max(arr)
res = 0

while s <= e:
    mid = (s + e) // 2

    temp = 0
    for i in arr:
        temp += i // mid

    if temp >= n:
        res = max(res, mid)
        s = mid + 1
    else:
        e = mid - 1
print(res)