import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
arr = sorted([0] + list(map(int, input().split())) + [l])

s = 1
e = l-1
ans = 0

while s <= e:
    cnt = 0
    mid = (s + e) // 2
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > mid:
            cnt += (arr[i] - arr[i-1]-1) // mid
    if cnt > m:
        s = mid + 1
    else:
        e = mid - 1
        ans = mid

print(ans)