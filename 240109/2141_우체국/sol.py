import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

inf = int(1e9)
loca = []
temp = 0

for i in range(n):
    # 마을 위치와 인구수 추가
    loca.append(arr[i])
    # 전체 인구수 갱신
    temp += arr[i][1]

# 마을 위치 기준 오름차순 정렬
loca.sort(key= lambda x : x[0])

cnt = 0
for i in range(n):
    # 현재 마을 인구수
    cnt += loca[i][1]
    # 누적 인구수가 전체 인구수의 절반 이상이면
    # 현재 위치에 우체국을 세우는 게 최적
    if cnt >= temp/2:
        print(loca[i][0])
        break