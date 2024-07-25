import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for length in range(2, n+1):  # 부분 문자열의 길이 2~n
    for i in range(n-length+1):  # 시작 인덱스
        j = i + length - 1  # 끝 인덱스
        if arr[i] == arr[j]:  # 시작과 끝이 같으면 그냥 제거
            dp[i][j] = dp[i+1][j-1]
        else:   # 시작과 끝이 다르면 횟수 추가
            dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

print(dp[0][n-1])