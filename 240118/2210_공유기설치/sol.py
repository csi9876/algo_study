import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

s = 1
e = arr[-1] - arr[0]     # 최댓값과 최솟값의 차
res = 0

while s <= e:
    mid = (s + e) // 2
    cur = arr[0]    # 공유기 설치
    cnt = 1     # 공유기 증가

    for i in range(1, n):   # 2번째 집부터 검사
        if arr[i] >= cur + mid:     # 현재 위치가 이전 공유기 + 중간점보다 크거나 같으면
            cnt += 1    # 공유기 설치
            cur = arr[i]    # 집 위치 저장

    if cnt >= c:    # 공유기 c개 이상 설치할 수 있으면 거리 증가
        s = mid + 1
        res = mid   # 최대 거리 저장
    else:   # 공유기 c개 미만 설치해야 하면 거리 감소
        e = mid - 1

print(res)
