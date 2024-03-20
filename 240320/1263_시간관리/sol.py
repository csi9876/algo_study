import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    t, d = map(int, input().split())
    arr.append((t, d))


arr.sort(key=lambda x: (-x[1], x[0]))

res = arr[0][1] # 마감 기한 가장 늦은 녀석으로 초기 설정


for i in range(1, n):
    if res < arr[i][1]: # 현재 결과가 다음 마감보다 작으면
        res -= arr[i][0]    # 결과 - 다음 일 시간
    else:
        res = arr[i][1] - arr[i][0] # 결과 = 마감 - 일 시간


if res < 0:
    print(-1)
else:
    print(res)