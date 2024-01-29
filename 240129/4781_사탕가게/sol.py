import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())

    # 마지막 줄 종료
    if n == 0 and m == 0.00:
        break

    # int 형변환
    n = int(n)
    m = int(m * 100 + 0.5)  # +0.5 해야 오류 안 남

    arr = []
    for i in range(n):
        c, p = map(float, input().split())
        arr.append([int(c), int(p * 100 + 0.5)])

    # dp 배열
    dp = [0] * (m+1)

    for j in range(n):  # 모든 상품 반복
        cc = arr[j][0]
        cm = arr[j][1]

        for i in range(cm, m + 1):  # 상품 가격부터 예산까지 반복
            # (현재 예산 - 상품 가격 뺀 예산의 만족도) + 현재 만족도
            # VS 현재 예산의 만족도
            dp[i] = max(dp[i], dp[i - cm] + cc)
    print(dp[m])
