import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    total = 0  # 전체 금액
    coins = []

    for _ in range(n):
        v, c = map(int, input().split())
        total += v * c
        coins.append([v, c])

    # 홀수는 중단
    if total % 2 == 1:
        print(0)
        continue

    total //= 2
    # dp[n] == 주어진 동전들로 n원을 만들 수 있는가?
    dp = [True] + [False] * total

    answer = 0
    for v, c in coins:

        # 거꾸로 탐색하면서 지불 가능한 액수 갱신
        for i in range(total, v - 1, -1):
            if dp[i - v]:
                for j in range(c):
                    if i + v * j <= total:
                        dp[i + v * j] = True
                    else:
                        break

        if dp[-1]:  # 양분
            answer = 1
            break

    print(answer)