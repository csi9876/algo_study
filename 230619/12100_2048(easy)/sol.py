import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)