import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = []
for _ in range(M):
    k = int(input())
    arr.append(k)
