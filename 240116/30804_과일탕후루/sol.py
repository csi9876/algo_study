import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_n = max(arr)
s = max_n
e = sum(arr)
ans = e

while s <= e:
    mid = (s + e) // 2
    cnt = 1
    temp_sum = 0
    for i in arr:
        if temp_sum + i > mid:
            cnt += 1
            temp_sum = 0
        temp_sum += i

    if cnt <= m:
        ans = min(ans, mid)
        e = mid - 1
    else:
        s = mid + 1

print(ans)