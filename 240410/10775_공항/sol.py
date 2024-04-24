import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


g = int(input())
p = int(input())
arr = list(int(input()) for _ in range(p))
print(arr)