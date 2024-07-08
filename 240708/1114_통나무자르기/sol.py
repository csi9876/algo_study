import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

l, k, c = map(int, input().split())
arr = set(map(int, input().split()))
arr = list(arr)
arr.append(0)
arr.append(l)
arr.sort()

v = [arr[i] - arr[i-1] for i in range(1, len(arr))]

s = 1
e = l

res = 0
fir = 0

while s <= e:
    mid = (s+e)//2
    if max(v) > mid:
        s = mid + 1
    else:
        temp = 0
        cnt = 0
        for i in v[::-1]:
            temp += i
            if temp > mid:
                temp = i
                cnt += 1
        if cnt > c:
            s = mid + 1
        else:
            res = mid
            if cnt == c:
                fir = temp
            else:
                fir = v[0]
            e = mid - 1

print(res, fir)