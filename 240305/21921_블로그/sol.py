import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int ,input().split()))

if sum(arr) == 0:
    print("SAD")
else:
    cnt = 1
    max_n = sum(arr[:m])
    temp = sum(arr[:m])

    for i in range(m, n):
        temp = temp - arr[i-m] + arr[i]
        if max_n == temp:
            cnt += 1
        elif max_n < temp:
            max_n = temp
            cnt = 1
    print(max_n)
    print(cnt)