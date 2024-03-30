import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = sorted(list(int(input()) for _ in range(n)), reverse=True)
idx = 0
cnt = 0
while True:
    temp = k//arr[idx]
    k -= temp * arr[idx]
    cnt += temp
    if k == 0:
        break
    idx += 1

print(cnt)