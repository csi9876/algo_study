import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(n):
    dp[i + 1] = dp[i]
    min_n = max_n = arr[i]  # 최소값과 최대값 설정
    idx = i - 1  # 시작 위치

    #  arr[idx]가 현재 구간의 최소값 또는 최대값보다 작거나 큰 동안 반복합
    while idx >= 0 and (arr[idx] < min_n or arr[idx] > max_n):
        #  arr[idx]를 현재 구간에 포함시키고, min_n과 max_n을 업데이트
        min_n, max_n = min(arr[idx], min_n), max(arr[idx], max_n)
        #  p[i+1]을 업데이트합니다. 현재 구간을 사용했을 때의 점수는
        #  dp[idx]+max_n-min_n이므로,
        #  이 값과 기존의 dp[i+1] 중 더 큰 값으로 dp[i+1]을 업데이트
        dp[i+1] = max(dp[i+1], dp[idx]+max_n-min_n)
        # idx를 하나 감소. 즉, 현재 구간의 시작 위치를 왼쪽으로 이동
        idx -= 1

print(dp[n])