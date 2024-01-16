import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sum_n = [0] * (n + 1)

# 누적합 계산
for i in range(1, n+1):
    sum_n[i] = sum_n[i-1] + arr[i-1]

ans = int(1e9)
s, e = 0, 1

# s가 수열 끝까지
while s < n:
    if sum_n[e] - sum_n[s] >= m:    # s부터 e까지 목표 합 이상인 경우
        ans = min(ans, e - s)   # 최소값 업데이트
        s += 1  # s 오른쪽으로 이동
    else:   # 부분 수열 합이 목표 미만인 경우
        if e < n:   # e가 수열의 끝이 아니면
            e += 1  # e를 오른쪽으로 이동
        else:
            s += 1  # 시작 위치를 오른쪽으로 이동

if ans == int(1e9):
    ans = 0

print(ans)