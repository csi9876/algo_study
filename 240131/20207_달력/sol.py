import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 366     # 달력 배열

for i in range(n):
    s, e = map(int, input().split())
    while s <= e:   # 달력 기간 체크
        arr[s] += 1     # 일정 추가
        s += 1

res = 0
x = 0   # 연속된 일정이 있는 일수 저장
y = 0   # 가장 많이 겹친 일정 개수 저장

for i in range(366):
    if arr[i] == 0:     # 일정이 없으면
        res += x * y    # 연속 일정 * 가장 많이 겹친 일정
        x, y = 0, 0     # 초기화
        continue
    x += 1      # 일정 있으면 연속 일정 + 1
    y = max(y, arr[i])  # 가장 많이 겹친 날 vs 현재 날 일정

print(res + x * y)