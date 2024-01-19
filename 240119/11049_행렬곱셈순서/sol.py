import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

inf = sys.maxsize
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[inf] * (n + 1) for _ in range(n)]

for i in range(n):
