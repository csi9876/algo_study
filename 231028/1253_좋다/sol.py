import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0

for i in range(N):
    temp = arr[:i]+arr[i+1:]
    s, e = 0, len(temp) - 1

    while s < e:
        p = temp[s] + temp[e]
        if arr[i] == p:
            res += 1
            break
        elif arr[i] > p:
            s += 1
        elif arr[i] < p:
            e -= 1

print(res)
