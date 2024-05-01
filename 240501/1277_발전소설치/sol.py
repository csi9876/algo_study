import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, w = map(int, input().split())
m = float(input())
arr = [list(map(int, input().split())) for _ in range(n)]
adj = [list(map(int, input().split())) for _ in range(w)]