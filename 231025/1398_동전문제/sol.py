import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

T = int(input())
coin = [1, 10, 25]

while T:
    T -= 1
    P = int(input())
    res = 0
    dp = [10**15+1 for _ in range(100)]
    dp[0] = 0
    for c in coin:
        for i in range(c, 100):
            dp[i] = min(dp[i], dp[i-c]+1)
    while P:
        res += dp[P % 100]
        P //= 100
    print(res)


# import sys
# input = sys.stdin.readline
#
# T = int(input())
# coin = [1, 10, 25]
# for _ in range(T):
#     P = int(input())
#     res = 0
#     dp = [10**15+1 for _ in range(100)]
#     dp[0] = 0
#     for c in coin:
#         for i in range(c, 100):
#             dp[i] = min(dp[i], dp[i-c]+1)
#     for _ in range(P):
#         res += dp[P % 100]
#         P //= 100
#     print(res)