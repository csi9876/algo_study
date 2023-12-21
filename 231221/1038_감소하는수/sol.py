import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
cnt = 1
idx = '0123456789'

nums = []

for i in idx:
    nums.append(i)

while cnt < 10:
    for i in nums:
        if len(i) == cnt:       # 현재 수의 자릿수
            for j in range(10):     # 0~9
                if int(i[-1]) > j:      # 마지막 숫자보다 작은 수면
                    nums.append(i + str(j))     # 추가하기
    cnt += 1


if n > 1022:
    print(-1)
else:
    print(nums[n])