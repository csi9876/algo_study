import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

arr.sort()

max_n = 1
cnt = 0

for i in arr:
    if i >= max_n:
        cnt += i - max_n
        max_n += 1

print(cnt)