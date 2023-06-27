import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
# print(arr)
dir = list(map(int, input()))
print(dir)

