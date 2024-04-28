import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
num = sorted(set(arr))

dict1 = {num[i]: i for i in range(len(num))}

for i in arr:
    print(dict1[i], end=" ")