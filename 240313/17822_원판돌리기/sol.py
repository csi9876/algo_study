import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
