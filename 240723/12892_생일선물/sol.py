import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline


n, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

sum = 0
res = 0
l, r = 0, 0

while True:
    # 현재 선물과 가장 오른쪽 선물 가격차이가 d보다 작으면
    # 오른쪽 선물 이동
    while r < n and arr[r][0] - arr[l][0] < d:
        sum += arr[r][1]
        r += 1

    # 최대 가치 갱신
    res = max(res, sum)
    if r == n:  # 오른쪽 선물 끝이면 종료
        break
    # 가장 왼쪽 선물 제거 및 이동
    sum -= arr[l][1]
    l += 1

print(res)