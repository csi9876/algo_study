import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

t = int(input())
arr = [list(map(int, input().strip())) for _ in range(t)]

k = int(input())
dire = [list(map(int, input().split())) for _ in range(k)]


