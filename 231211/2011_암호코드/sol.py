import sys
sys.stdin = open('input.txt')


import sys
# input = sys.stdin.readline

arr = [0] + list(map(int, input()))
n = len(arr)
dp = [0] * (n)

if arr[1] == 0:
    print(0)
else:
    dp[0] = 1  # 처음 수로 만들 수 있는 거 1개
    dp[1] = 1  # 처음 수로 만들 수 있는 거 1개

    for i in range(2, n):
        temp = arr[i]  # 1자리 암호
        ttemp = arr[i-1] * 10 + arr[i]  # 2자리 암호
        if 1 <= temp <= 9:  # 1자리는 1~9
            dp[i] += dp[i-1]
        if 10 <= ttemp <= 26:  # 2자리는 10~26
            dp[i] += dp[i-2]

    print(dp[n - 1] % 1000000)  # 나머지 연산