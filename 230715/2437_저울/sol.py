import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
sumn = 0
for i in range(N):
    if sumn + 1 >= arr[i]:
        sumn += arr[i]
    else:

        break
print(sumn + 1)