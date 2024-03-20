import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
number = input().strip()

stack = []


for i in number:
    i = int(i)

    while stack and k >= 1 and stack[-1] < i:
        stack.pop()
        k -= 1

    stack.append(i)

if k > 0:
    for i in range(k):
        stack.pop()

for i in stack:
    print(i, end="")