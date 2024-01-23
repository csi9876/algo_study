import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

inf = sys.maxsize


n = int(input())
arr = list(map(int, input().split()))

res = inf       # 합의 최소값 설정
idx_left = 0    # 작은 인덱스
idx_right = 0   # 큰 인덱스

for i in range(n - 1):
    current = arr[i]

    s = i + 1   # 시작위치
    e = n - 1   # 끝 위치

    while s <= e:
        mid = (s + e) // 2
        tmp = current + arr[mid]

        # tmp 절대값이 res보다 작으면 res, idx left right 갱신
        if abs(tmp) < res:
            res = abs(tmp)
            idx_left = i
            idx_right = mid

            if tmp == 0:
                break

        if tmp < 0:
            s = mid + 1

        else:
            e = mid - 1

print(arr[idx_left], arr[idx_right])