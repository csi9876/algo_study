import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline


n = int(input())
arr = [list(input().strip()) for _ in range(n)]
print(arr)