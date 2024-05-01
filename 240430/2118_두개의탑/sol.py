import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))

prefix = [0] * (2 * n + 1)      # 원형리스트이므로 2배
for i in range(2 * n):
        prefix[i+1] = prefix[i] + arr[i%n]

res = 0
total = sum(arr)
r = 1   # 우측 포인터

# 좌측 포인터
for l in range(2 * n):
        # 포인터가 범위 안  and 부분합이 나머지합보다 작다
        while r < 2*n+1 and prefix[r] - prefix[l] <= total - prefix[r] + prefix[l]:
                res = max(res, prefix[r]-prefix[l])
                r += 1
print(res)