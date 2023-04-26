import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [0]+list(map(int, input().split()))
# 0 10 20 10 30 20 50
# 0  1  2  1  3  2  4

# i번쨰 숫자 추가 시 최대길이
# dp[0]~dp[i-1] 중 최대값
dp = [0] * (N+1)
# 1~N까지
for i in range(1, N+1):
    maxn = 0
    # 0번째에서 i번째 까지
    for j in range(0, i):
        if arr[i] > arr[j]:
            maxn = max(maxn, dp[j]+1)
    dp[i] = maxn
result = max(dp)
print(result)



