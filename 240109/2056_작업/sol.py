import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 시간 저장
dp = [0] * (n + 1)
# 선행작업
v = {}
res = 0

# 모든 작업 순회
for i in range(1, n + 1):
    # i 번째 작업 저장
    dp[i] = arr[i - 1][0]
    # 선행작업이 없는 경우
    if arr[i - 1][1] == 0:
        continue
    # 선행 작업 번호 추가
    for j in arr[i - 1][2:]:
        if i in v:
            v[i].append(j)
        else:
            v[i] = [j]

# 최소시간 계산
for i in range(1, n + 1):
    # 선행 작업이 있다면
    if i in v:
        time = 0
        for j in v[i]:  # 범위 안에 있는지 확인
            if j <= n:
                time = max(time, dp[j])
                # 가장 오래 걸리는 선행작업 찾아 더하기
        dp[i] += time

print(max(dp))
