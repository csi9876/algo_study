import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
k = int(input())

s = 1
e = k
while s <= e:
    mid = (s + e) // 2
    cnt = 0

    for i in range(1, n+1):
        # 중간 값보다 같거나 작은 원소의 갯수 세기
        cnt += min(mid // i, n)

    if cnt < k:
        s = mid + 1
    else:
        e = mid - 1

print(s)