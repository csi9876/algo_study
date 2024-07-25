import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline


r, c, k = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

v = [[0 for _ in range(c)] for _ in range(r)]

