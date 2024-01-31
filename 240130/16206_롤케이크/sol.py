import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 10으로 나누어 떨어지는 것, 낮은 것 순으로 정렬
arr.sort(key=lambda x: (x % 10 != 0, x))

cnt = 0
res = 0
for i in range(n):
    if cnt == m:
        break

    while arr[i] > 10 and cnt < m:
        arr[i] -= 10
        cnt += 1
        res += 1

    if arr[i] == 10:
        res += 1

print(res)

