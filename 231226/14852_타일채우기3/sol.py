import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 2

for i in range(2, n + 1):
    dp[i] = (3*dp[i-1] + dp[i-2] - dp[i-3]) % 1000000007

print(dp[-1])

# dp[2] = 7
# dp[3] = 22

'''
ㅡ ㅇㅇ
ㅡㅡ ㅡㅇㅇ ㅇㅇㅡ ㅣㅣ ㅣㅇㅇ ㅇㅇㅣ ㅇㅇㅇㅇ
'''
