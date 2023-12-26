import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
plus = []
minus = []
maxn = 0    # 가장 먼 책 위치

#
for i in arr:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)
    # 마지막 책을 가장 먼 책으로 저장(편도)
    if abs(i) > abs(maxn):
        maxn = i

plus.sort(reverse=True)     # 내림차순
minus.sort()        # 오름차순

cnt = 0

# 양수 방향 책
for j in range(0, len(plus), m):
    # 최장 거리면 생략
    if plus[j] == maxn:
        continue
    cnt += plus[j]

# 음수 방향 책
for j in range(0, len(minus), m):
    # 최장 거리면 생략
    if minus[j] == maxn:
        continue
    cnt += abs(minus[j])

cnt *= 2    # 왕복
cnt += abs(maxn)    # 편도

print(cnt)