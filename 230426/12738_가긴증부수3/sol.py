import sys
sys.stdin = open('input.txt')

import bisect
N = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(N):
    # dp의 마지막 보다 크면 그냥 바로 어펜드
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    # 작으면 이진탐색으로 자기보다 큰 수 나온 인덱스 반환
    else:
        idx = bisect.bisect_left(dp, arr[i])
        # 해당 인덱스에 삽입
        dp[idx] = arr[i]
print(len(dp))

