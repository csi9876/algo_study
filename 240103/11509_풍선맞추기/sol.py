import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

v = [0] * (max(arr)+1)  # 높이 최대값 +1 로 v 배열 생성
cnt = 0

for i in arr:
    # 현재 풍선 높이에 이미 화살이 존재한다면
    if v[i]:
        v[i] -= 1   # 해당 높이의 화살 수를 하나 감소
        v[i - 1] += 1   # -1 높이의 화살 수 하나 증가
    else:
        cnt += 1    # 화살 추가
        v[i - 1] += 1   # 현재 높이 -1에 화살 수 증가

print(cnt)