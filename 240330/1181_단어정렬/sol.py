import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

t = int(input())
arr = []
for _ in range(t):
    s = input().strip()
    if s not in arr:
        arr.append(s)

arr.sort(key=lambda x: (len(x), x))
for i in arr:
    print(i)