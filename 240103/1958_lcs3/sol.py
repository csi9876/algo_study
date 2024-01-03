import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


a = list(input().strip())
b = list(input().strip())
c = list(input().strip())

# dp 3차원 배열
# 각
dp = [[[0] * (len(c)+1) for _ in range(len(b)+1)] for _ in range(len(a)+1)]

# 3 순회
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        for k in range(1, len(c)+1):

            # 세 문자열의 현재 문자가 모두 같으면 이전 길이 + 1
            if a[i-1] == b[j-1] == c[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            # 아니면 이전 길이들 중 최대값으로 설정
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[len(a)][len(b)][len(c)])



