import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    # 1~10000원
    M = int(input())
    # print(N, arr, M)
    # print(arr)
    # dp 0, 1~10000
    dp = [0] * (M+1)
    dp[0] = 1

    # 1원으로 갈 수 있는 곳
    for w in arr:
        # 1부터 끝까지
        for i in range(w, M+1):
            # 현재 값은 이전 값 더한 것
            dp[i] += dp[i-w]
        # print(dp)
    # print(dp)
    print(dp[-1])