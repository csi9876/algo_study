import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = []
for _ in range(n):
    a, b, c, d, e = map(int, input().split())
    