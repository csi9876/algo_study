import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
piece = [list(map(int, input().split())) for _ in range(k)]

print(arr)
print(piece)