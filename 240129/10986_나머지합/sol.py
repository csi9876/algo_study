import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

v = [0] * m  # m으로 나눈 나머지가 0, 1, 2인 경우의 수를 저장할 배열
v[0] = 1  # 초기 상태는 합계가 0이므로, 나머지가 0인 경우의 수를 1로 설정

sum_v = 0  # 부분 배열의 합계
cnt = 0  # m으로 나누어 떨어지는 부분 배열의 수

for i in range(n):
    sum_v += arr[i]  # 부분 배열의 합계 계산
    temp = sum_v % m  # 합계를 m으로 나눈 나머지 계산
    cnt += v[temp]  # 나머지에 따른 경우의 수를 더함
    v[temp] += 1  # 나머지에 따른 경우의 수 업데이트

print(cnt)
