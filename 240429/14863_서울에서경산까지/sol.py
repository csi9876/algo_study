import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * (k+1)

for i in range(1, n+1):
    wt, wm, bt, bm = map(int, input().split())

    new_dp = [0] * (k+1)
    for j in range(k+1):
        # 보행 이동 시간 계산
        # 남은 시간이 이동 시간보다 크고, 이전 도시에 방문했다면
        if j >= wt and dp[j - wt] != -1:
            walk = dp[j - wt] + wm
        else:   # 방문불가
            walk = -1

        # 자전거 이동 시간 계산
        if j >= bt and dp[j - bt] != -1:
            bike = dp[j - bt] + bm
        else:
            bike = -1
        new_dp[j] = max(walk, bike)

    dp = new_dp

print(dp[k])