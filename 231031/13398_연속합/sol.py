import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()

def solution(arr, n, m):
    left, right = 0, 0
    res = 2000000000
    while right < n:
        temp = arr[right] - arr[left]
        if temp < m:
            right += 1
        elif temp > m:
            res = min(temp, res)
            left += 1
        else:
            return m
    return res

# 답변 구하기
res = solution(arr, n, m)

print(res)
