import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))


# 각 변에 대한 계산
sum_list = [min(arr[0], arr[5]), min(arr[1], arr[4]), min(arr[2], arr[3])]
sum_list.sort()     # 최소값 오름차순 계산

# 각 면에 대한 계산
a = (n-2)*(n-2) + (n-1)*(n-2)*4     # 가장 안쪽면
b = (n-2)*4 + (n-1)*4       # 중간 면 합
c = 4       # 가장 바깥쪽 면 합

# 최종 결과
res = a * sum_list[0] + b * sum(sum_list[:2]) + c * (sum(sum_list))

if n == 1:
    print(sum(arr) - max(arr))
else:
    print(res)