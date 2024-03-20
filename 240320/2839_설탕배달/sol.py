import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
# 3키로 / 5키로

res = 0
while n >= 0:
    if n % 5 == 0:
        res += n // 5
        print(res)
        break
    n -= 3
    res += 1
else:
    print(-1)