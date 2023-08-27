import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
# 집 수, 공유기 개수
n, c = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort()


def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= current + mid:
                count += 1
                current = arr[i]

        if count >= c:
            global res
            start = mid + 1
            res = mid
        else:
            end = mid - 1


s = 1
e = arr[-1] - arr[0]
res = 0

binary_search(arr, s, e)
print(res)