import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr.sort()
res = 0

if sum(arr) <= m:
    print(max(arr))
else:
    s = 0
    e = arr[-1]

    while s <= e:
        mid = (s+e) // 2
        temp = 0

        for i in arr:
            if i <= mid:
                temp += i
            else:
                temp += mid

        if temp <= m:
            s = mid + 1
            res = mid
        else:
            e = mid - 1
    print(res)
