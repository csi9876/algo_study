import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr = arr + arr[:k-1]   # 원형 리스트를 위해 늘리기

counts = [0] * (d+1)  # 각 초밥의 개수를 저장
kinds = 0  # 현재 윈도우에 있는 초밥 종류의 개수

# 초밥 종류의 개수를 세고, counts를 업데이트
for i in range(k):
    if counts[arr[i]] == 0:
        kinds += 1
    counts[arr[i]] += 1

max_n = kinds

# k번째부터 끝까지
for i in range(k, n+k-1):
    if counts[arr[i]] == 0:
        kinds += 1
    counts[arr[i]] += 1

    counts[arr[i-k]] -= 1
    if counts[arr[i-k]] == 0:
        kinds -= 1

    max_n = max(max_n, kinds + (counts[c] == 0))  # 쿠폰을 사용하여 새로운 종류를 추가할 수 있는 경우를 고려

print(max_n)