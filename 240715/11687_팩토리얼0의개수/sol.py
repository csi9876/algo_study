import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline


# N!의 오른쪽 0의 개수 = N!의 인수 중 10의 배수의 개수
# = 2*5의 개수 = 소인수 2와 5의 배수의 개수
# = 소인수 5의 배수의 개수
# 즉, N을 5로 나눈 몫


m = int(input())
l, r = 1, m*5
res = 0

def search(x):
    cnt = 0
    while x >= 5:
        cnt += x//5
        x //= 5
    return cnt

while l <= r:
    mid = (l+r) // 2

    cnt = search(mid)

    if cnt < m:
        l = mid + 1
    else:
        r = mid - 1
        res = mid

# 유효값인지 확인
if search(res) != m:
    res = -1

print(res)