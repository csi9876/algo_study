import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())
arr = [list(input().strip()) for _ in range(m)]
info = [list(map(int, input().split())) for _ in range(k)]
print(arr)
print(info)