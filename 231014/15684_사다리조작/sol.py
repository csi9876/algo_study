import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
print(N, M, H)
arr = []
for i in range(M):
    s, e = map(int,input().split())
    arr.append([s, e])
print(arr)