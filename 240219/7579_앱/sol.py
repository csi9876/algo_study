import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
dp = [0 for _ in range(sum(cost)+1)]    # 비용의 총합만큼의 길이

for i in range(n):
    # 해당 앱을 비활성화 했을 때의 비용부터 모든 비용에 대하여 역순으로
    for j in range(sum(cost), cost[i]-1, -1):
        dp[j] = max(dp[j], dp[j-cost[i]] + memory[i]) # 해당 비용으로 얻을 수 있는 최대 메모리를 저장

for i in range(len(dp)): # dp 리스트를 처음부터 끝까지 검사
    if dp[i] >= m:  # 만약 해당 비용으로 얻을 수 있는 메모리가  M 이상이라면
        print(i)  # 그 비용 출력
        break