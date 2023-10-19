import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    s = int(input())
    arr.append(s)
print(arr)