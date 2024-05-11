import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

s = 0
e = 0

res = 0

v = [0] * 100001

while e < n:
    if not v[arr[e]]:       # 현재 값을 방문하지 않았을 때
        v[arr[e]] = 1
        e += 1
        res += e - s
    else:                   # 방문했을 때
        while v[arr[e]]:
            v[arr[s]] = 0
            s += 1
print(res)