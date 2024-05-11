import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

import math

n = int(input())

# 에라토스테네스의 채
arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

for num in range(2, int(math.sqrt(n)) + 1):
    if arr[num]:
        for mul in range(num * 2, n + 1, num):
            arr[mul] = False

arr = [i for i in range(2, n + 1) if arr[i]] + [0]

# 투 포인터
s = 0
e = 0
total = arr[s]
count = 0

while e < len(arr) - 1:
    # 연속합이 N과 같으면 카운팅
    # 왼쪽, 오른쪽 포인터 둘 다 한칸 진행
    # 왼쪽만 옮기면 연속합이 작아지므로 오른쪽도 같이 옮김
    if total == n:
        count += 1
        total -= arr[s]
        s += 1
        e += 1
        total += arr[e]
    # 연속합이 N보다 작으면
    # 오른쪽 포인터를 진행(값 상승)
    elif total < n:
        e += 1
        total += arr[e]
    # 연속합이 N보다 크면
    # 왼쪽 포인터 진행(값 감소)
    else:
        total -= arr[s]
        s += 1

print(count)