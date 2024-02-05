import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

import bisect

t = int(input())
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
brr = list(map(int, input().split()))

sum_A = []      # 부분 배열의 합
for i in range(n):
    temp_a = 0
    for j in range(i, n):
        temp_a += arr[j]
        sum_A.append(temp_a)

sum_B = []      # 부분 배열의 합
for i in range(m):
    temp_b = 0
    for j in range(i, m):
        temp_b += brr[j]
        sum_B.append(temp_b)

res = 0
sum_A.sort()
sum_B.sort()

for a in sum_A:
    temp = t - a    # t - 첫 부분 배열의 합 빼기
    # temp가 두번째 배열에서 처음 등장하는 위치 찾기
    l = bisect.bisect_left(sum_B, temp)
    # temp가 두번째 배열에서 마지막 등장하는 위치 찾기
    r = bisect.bisect_right(sum_B, temp)
    # 마지막 인덱스 - 처음 인덱스
    res += r - l
print(res)