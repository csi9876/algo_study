import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N, L = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

for i in arr:
    for j in i:
        