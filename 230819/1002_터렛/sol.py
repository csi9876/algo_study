import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    print(arr)
