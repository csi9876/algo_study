import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

if m == 0:
    broken = []
else:
    broken = list(map(int, input().split()))

# 최솟값 = 현재 채널 - 목적 채널
min_n = abs(100 - n)

# 만들 수 있는 가장 큰 수 까지
for i in range(999999):
    num = str(i)

    for j in num:
        # 고장난 버튼이면 중지
        if int(j) in broken:
            break
    else:
        # 멀쩡한 버튼이면
        # 최솟값 vs 채널 이동 수 + 중간 채널
        min_n = min(min_n, abs(n - i) + len(num))

print(min_n)