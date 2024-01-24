import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

inf = sys.maxsize

n = int(input())
arr = sorted(list(map(int, input().split())))


res = inf       # 합의 최소값 설정
idx_left = 0    # 작은 인덱스
idx_mid = 0     # 중간 인덱스
idx_right = 0   # 큰 인덱스


for i in range(n - 2):  # 모든 용액 반복
    s = i + 1   # 시작위치
    e = n - 1   # 끝 위치

    while s < e:
        sum_n = arr[i] + arr[s] + arr[e]    # 세 용액 합

        if abs(sum_n) < res:    # 현재 값이 최소값보다 작으면
            res = abs(sum_n)    # 저장
            idx_left = i
            idx_mid = s
            idx_right = e

        if sum_n > 0:   # 특성값의 합이 0보다 크면, 끝 인덱스 감소
            e -= 1
        else:
            s += 1

print(arr[idx_left], arr[idx_mid],  arr[idx_right])